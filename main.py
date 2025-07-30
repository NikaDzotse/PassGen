#!/usr/bin/env python3
"""
Password Wordlist Generator with GUI
A modern, user-friendly application for generating custom password wordlists.
"""

import os
import sys
import subprocess
import importlib.util

VENV_DIR = os.path.join(os.path.dirname(__file__), "venv")
VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python3")

def ensure_venv():
    # If we're not inside the virtual environment
    if sys.prefix != VENV_DIR:
        if not os.path.exists(VENV_PYTHON):
            print("📦 Creating virtual environment...")
            subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        
        print("🚀 Re-launching script inside virtual environment...")
        os.execv(VENV_PYTHON, [VENV_PYTHON] + sys.argv)

def install_if_missing(package):
    if importlib.util.find_spec(package) is None:
        print(f"📦 Installing missing package: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

ensure_venv()
install_if_missing("customtkinter")

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import string
import math
import os
from typing import List, Set
import threading
import time

# Configure CustomTkinter appearance
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class PasswordWordlistGenerator:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Password Wordlist Generator")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Set minimum window size
        self.root.minsize(500, 600)
        
        # Variables
        self.status_var = ctk.StringVar(value="Ready to generate wordlist")
        self.progress_var = ctk.DoubleVar(value=0)
        
        # Custom words variables
        self.add_numbers_var = ctk.BooleanVar(value=True)
        self.add_symbols_var = ctk.BooleanVar(value=False)
        self.capitalize_var = ctk.BooleanVar(value=True)
        self.reverse_var = ctk.BooleanVar(value=False)
        self.leet_speak_var = ctk.BooleanVar(value=False)
        
        # Generation state
        self.is_generating = False
        self.generated_count = 0
        self.total_combinations = 0
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Create scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(self.root)
        self.scrollable_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(
            self.scrollable_frame, 
            text="🔐 Password Wordlist Generator", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(pady=(20, 30))
        
        # Description
        desc_label = ctk.CTkLabel(
            self.scrollable_frame,
            text="Generate password wordlists based on your custom words",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        desc_label.pack(pady=(0, 30))
        
        # Custom Words Section
        self.create_custom_words_section(self.scrollable_frame)
        
        # Preview Section
        self.create_preview_section(self.scrollable_frame)
        
        # Progress Section
        self.create_progress_section(self.scrollable_frame)
        
        # Control Buttons
        self.create_control_buttons(self.scrollable_frame)
        
        # Status Section
        self.create_status_section(self.scrollable_frame)
        
    def create_custom_words_section(self, parent):
        """Create custom words input section"""
        self.custom_words_frame = ctk.CTkFrame(parent)
        self.custom_words_frame.pack(fill="x", padx=20, pady=10)
        
        custom_words_label = ctk.CTkLabel(
            self.custom_words_frame, 
            text="Custom Words:", 
            font=ctk.CTkFont(size=16, weight="bold")
        )
        custom_words_label.pack(pady=(15, 5))
        
        # Instructions
        instructions_label = ctk.CTkLabel(
            self.custom_words_frame,
            text="Enter your custom words (one per line or separated by commas):",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        instructions_label.pack(pady=(0, 10))
        
        # Custom words text area
        self.custom_words_text = ctk.CTkTextbox(
            self.custom_words_frame,
            height=120
        )
        self.custom_words_text.pack(fill="x", padx=20, pady=(0, 15))
        
        # Add example text to help users
        self.custom_words_text.insert("1.0", "Enter your words here...\nExample:\npassword\nadmin\nuser\njohn\ncompany")
        
        # Word modifications
        mod_label = ctk.CTkLabel(
            self.custom_words_frame,
            text="Word Modifications:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        mod_label.pack(pady=(10, 5))
        
        # Modifications frame
        mod_frame = ctk.CTkFrame(self.custom_words_frame)
        mod_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        # Row 1
        add_numbers_cb = ctk.CTkCheckBox(
            mod_frame,
            text="Add numbers (0-9)",
            variable=self.add_numbers_var,
            command=self.update_preview
        )
        add_numbers_cb.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        add_symbols_cb = ctk.CTkCheckBox(
            mod_frame,
            text="Add symbols (!@#$%^&*)",
            variable=self.add_symbols_var,
            command=self.update_preview
        )
        add_symbols_cb.grid(row=0, column=1, padx=20, pady=10, sticky="w")
        
        # Row 2
        capitalize_cb = ctk.CTkCheckBox(
            mod_frame,
            text="Capitalize variations",
            variable=self.capitalize_var,
            command=self.update_preview
        )
        capitalize_cb.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        reverse_cb = ctk.CTkCheckBox(
            mod_frame,
            text="Reverse words",
            variable=self.reverse_var,
            command=self.update_preview
        )
        reverse_cb.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        
        # Row 3
        leet_cb = ctk.CTkCheckBox(
            mod_frame,
            text="Leet speak (a→@, e→3, etc.)",
            variable=self.leet_speak_var,
            command=self.update_preview
        )
        leet_cb.grid(row=2, column=0, padx=20, pady=10, sticky="w", columnspan=2)
        
    def create_preview_section(self, parent):
        """Create preview section showing charset and estimated size"""
        preview_frame = ctk.CTkFrame(parent)
        preview_frame.pack(fill="x", padx=20, pady=10)
        
        preview_label = ctk.CTkLabel(
            preview_frame, 
            text="Preview:", 
            font=ctk.CTkFont(size=16, weight="bold")
        )
        preview_label.pack(pady=(15, 5))
        
        # Character set preview
        self.charset_preview = ctk.CTkLabel(
            preview_frame,
            text="Custom words: ",
            font=ctk.CTkFont(size=12),
            wraplength=500
        )
        self.charset_preview.pack(pady=(0, 5))
        
        # Size estimation
        self.size_preview = ctk.CTkLabel(
            preview_frame,
            text="Estimated combinations: ",
            font=ctk.CTkFont(size=12)
        )
        self.size_preview.pack(pady=(0, 15))
        
    def create_progress_section(self, parent):
        """Create progress bar section"""
        progress_frame = ctk.CTkFrame(parent)
        progress_frame.pack(fill="x", padx=20, pady=10)
        
        self.progress_bar = ctk.CTkProgressBar(progress_frame)
        self.progress_bar.pack(fill="x", padx=20, pady=10)
        self.progress_bar.set(0)
        
        self.progress_label = ctk.CTkLabel(
            progress_frame,
            text="Ready",
            font=ctk.CTkFont(size=12)
        )
        self.progress_label.pack(pady=(0, 10))
        
    def create_control_buttons(self, parent):
        """Create control buttons"""
        button_frame = ctk.CTkFrame(parent)
        button_frame.pack(fill="x", padx=20, pady=10)
        
        # Generate button
        self.generate_btn = ctk.CTkButton(
            button_frame,
            text="Generate Wordlist",
            command=self.start_generation,
            font=ctk.CTkFont(size=16, weight="bold"),
            height=40
        )
        self.generate_btn.pack(side="left", padx=(20, 10), pady=20)
        
        # Stop button
        self.stop_btn = ctk.CTkButton(
            button_frame,
            text="Stop",
            command=self.stop_generation,
            font=ctk.CTkFont(size=16),
            height=40,
            fg_color="red",
            hover_color="darkred",
            state="disabled"
        )
        self.stop_btn.pack(side="left", padx=(10, 20), pady=20)
        
    def create_status_section(self, parent):
        """Create status display section"""
        status_frame = ctk.CTkFrame(parent)
        status_frame.pack(fill="x", padx=20, pady=10)
        
        status_label = ctk.CTkLabel(
            status_frame,
            textvariable=self.status_var,
            font=ctk.CTkFont(size=12),
            wraplength=500
        )
        status_label.pack(pady=15)
        
    def get_custom_words(self) -> List[str]:
        """Get custom words from text area"""
        text = self.custom_words_text.get("1.0", "end-1c").strip()
        if not text:
            return []
        
        # Split by newlines and commas, then clean up
        words = []
        for line in text.split('\n'):
            for word in line.split(','):
                word = word.strip()
                if word:
                    words.append(word)
        
        return list(set(words))  # Remove duplicates
        
    def apply_word_modifications(self, word: str) -> List[str]:
        """Apply modifications to a word"""
        variations = [word]
        
        # Capitalize variations
        if self.capitalize_var.get():
            variations.append(word.capitalize())
            variations.append(word.upper())
            variations.append(word.lower())
        
        # Reverse words
        if self.reverse_var.get():
            variations.append(word[::-1])
            if self.capitalize_var.get():
                variations.append(word.capitalize()[::-1])
                variations.append(word.upper()[::-1])
        
        # Leet speak
        if self.leet_speak_var.get():
            leet_map = {
                'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'
            }
            leet_word = word.lower()
            for char, replacement in leet_map.items():
                leet_word = leet_word.replace(char, replacement)
            variations.append(leet_word)
        
        return list(set(variations))  # Remove duplicates
        
    def generate_custom_wordlist(self, base_words: List[str]) -> List[str]:
        """Generate wordlist based on custom words"""
        all_passwords = []
        
        for word in base_words:
            # Get word variations
            variations = self.apply_word_modifications(word)
            
            for variation in variations:
                all_passwords.append(variation)
                
                # Add numbers
                if self.add_numbers_var.get():
                    for i in range(10):
                        all_passwords.append(f"{variation}{i}")
                    for i in range(10):
                        all_passwords.append(f"{i}{variation}")
                
                # Add symbols
                if self.add_symbols_var.get():
                    symbols = "!@#$%^&*"
                    for symbol in symbols:
                        all_passwords.append(f"{variation}{symbol}")
                        all_passwords.append(f"{symbol}{variation}")
                
                # Add numbers + symbols combinations
                if self.add_numbers_var.get() and self.add_symbols_var.get():
                    for i in range(10):
                        for symbol in symbols:
                            all_passwords.append(f"{variation}{i}{symbol}")
                            all_passwords.append(f"{symbol}{i}{variation}")
        
        return list(set(all_passwords))  # Remove duplicates
        
    def update_preview(self, *args):
        """Update the preview section with current settings"""
        try:
            # Custom words mode
            custom_words = self.get_custom_words()
            if custom_words:
                # Generate preview of custom wordlist
                total_estimated = len(self.generate_custom_wordlist(custom_words))
                
                self.charset_preview.configure(
                    text=f"Custom words: {len(custom_words)} base words"
                )
                
                self.size_preview.configure(
                    text=f"Estimated combinations: {total_estimated:,} passwords"
                )
                
                # Color coding
                if total_estimated > 100_000:
                    self.size_preview.configure(text_color="red")
                elif total_estimated > 10_000:
                    self.size_preview.configure(text_color="orange")
                else:
                    self.size_preview.configure(text_color="white")
            else:
                self.charset_preview.configure(text="Custom words: Please enter some words")
                self.size_preview.configure(text="Estimated combinations: ")
                    
        except Exception as e:
            self.charset_preview.configure(text="Error calculating preview")
            self.size_preview.configure(text="Estimated combinations: ")
            
    def validate_inputs(self) -> bool:
        """Validate user inputs before generation"""
        # Custom words mode validation
        custom_words = self.get_custom_words()
        if not custom_words:
            messagebox.showerror("No Words", "Please enter some custom words")
            return False
        
        # Check if any modifications are selected
        if not any([
            self.add_numbers_var.get(),
            self.add_symbols_var.get(),
            self.capitalize_var.get(),
            self.reverse_var.get(),
            self.leet_speak_var.get()
        ]):
            messagebox.showerror("No Modifications", "Please select at least one word modification")
            return False
                
        return True
        
    def start_generation(self):
        """Start the wordlist generation process"""
        if not self.validate_inputs():
            return
            
        # Get save file path
        file_path = filedialog.asksaveasfilename(
            title="Save Wordlist As",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
            
        # Start generation in separate thread
        self.is_generating = True
        self.generated_count = 0
        
        # Update UI
        self.generate_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")
        self.status_var.set("Generating wordlist...")
        self.progress_bar.set(0)
        
        # Start generation thread
        thread = threading.Thread(
            target=self.generate_wordlist,
            args=(file_path,),
            daemon=True
        )
        thread.start()
        
    def stop_generation(self):
        """Stop the wordlist generation"""
        self.is_generating = False
        self.status_var.set("Generation stopped by user")
        self.generate_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        
    def generate_wordlist(self, file_path: str):
        """Generate the wordlist and save to file"""
        try:
            # Custom words mode
            custom_words = self.get_custom_words()
            all_passwords = self.generate_custom_wordlist(custom_words)
            self.total_combinations = len(all_passwords)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                for i, password in enumerate(all_passwords):
                    if not self.is_generating:
                        break
                    f.write(password + '\n')
                    self.generated_count = i + 1
                    
                    # Update progress every 1000 passwords
                    if self.generated_count % 1000 == 0:
                        progress = min(self.generated_count / self.total_combinations, 1.0)
                        self.root.after(0, self.update_progress, progress, self.generated_count)
                
            if self.is_generating:
                self.root.after(0, self.generation_complete, file_path)
            else:
                self.root.after(0, self.generation_stopped)
                
        except Exception as e:
            self.root.after(0, self.generation_error, str(e))
        
    def update_progress(self, progress: float, count: int):
        """Update progress bar and label"""
        self.progress_bar.set(progress)
        self.progress_label.configure(text=f"Generated: {count:,} passwords")
        
    def generation_complete(self, file_path: str):
        """Handle successful generation completion"""
        self.is_generating = False
        self.generate_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.progress_bar.set(1.0)
        self.progress_label.configure(text=f"Complete! Generated {self.generated_count:,} passwords")
        self.status_var.set(f"Wordlist saved to: {file_path}")
        
        messagebox.showinfo(
            "Generation Complete",
            f"Successfully generated {self.generated_count:,} passwords!\n"
            f"Saved to: {file_path}"
        )
        
    def generation_stopped(self):
        """Handle generation stop"""
        self.generate_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.progress_label.configure(text=f"Stopped at {self.generated_count:,} passwords")
        
    def generation_error(self, error_msg: str):
        """Handle generation error"""
        self.is_generating = False
        self.generate_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.status_var.set(f"Error: {error_msg}")
        
        messagebox.showerror("Generation Error", f"An error occurred:\n{error_msg}")
        
    def run(self):
        """Start the application"""
        self.update_preview()  # Initial preview update
        self.root.mainloop()

def main():
    """Main entry point"""
    app = PasswordWordlistGenerator()
    app.run()

if __name__ == "__main__":
    main() 
