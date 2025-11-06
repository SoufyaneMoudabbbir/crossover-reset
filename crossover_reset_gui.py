#!/usr/bin/env python3
"""
CrossOver Trial Reset - GUI Application
Resets CrossOver trial period on macOS
"""

import os
import shutil
import re
import plistlib
import subprocess
import time
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime
import threading


class CrossOverResetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CrossOver Trial Reset")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Set app icon (if available)
        try:
            if os.path.exists("icon.icns"):
                self.root.iconbitmap("icon.icns")
        except:
            pass
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="CrossOver Trial Reset",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=(0, 10))
        
        # Description
        desc_label = ttk.Label(
            main_frame,
            text="Reset your CrossOver trial period with one click.\nAll your bottles and Windows apps will remain intact.",
            font=("Helvetica", 11),
            justify=tk.CENTER
        )
        desc_label.pack(pady=(0, 20))
        
        # Status area (scrolled text)
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.status_text = scrolledtext.ScrolledText(
            status_frame,
            height=15,
            width=70,
            font=("Courier", 10),
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.status_text.pack(fill=tk.BOTH, expand=True)
        
        # Reset button
        self.reset_button = ttk.Button(
            main_frame,
            text="Reset CrossOver Trial",
            command=self.start_reset,
            style="Accent.TButton"
        )
        self.reset_button.pack(pady=(0, 10))
        
        # Progress bar
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=300
        )
        self.progress.pack(pady=(0, 10))
        
        # Footer
        footer_label = ttk.Label(
            main_frame,
            text="© 2025 - Use at your own risk",
            font=("Helvetica", 9),
            foreground="gray"
        )
        footer_label.pack()
        
        # Initial message
        self.log("Ready to reset CrossOver trial.")
        self.log("Click the button above to start.")
        
    def log(self, message, error=False):
        """Add message to status text"""
        self.status_text.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix = "[ERROR]" if error else "[INFO]"
        
        self.status_text.insert(tk.END, f"{timestamp} {prefix} {message}\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)
        
        # Update the GUI
        self.root.update_idletasks()
        
    def start_reset(self):
        """Start the reset process in a separate thread"""
        self.reset_button.config(state=tk.DISABLED)
        self.progress.start(10)
        
        # Clear status
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.config(state=tk.DISABLED)
        
        # Run reset in thread to keep GUI responsive
        thread = threading.Thread(target=self.reset_crossover, daemon=True)
        thread.start()
        
    def reset_crossover(self):
        """Main reset logic"""
        try:
            # Step 1: Kill CrossOver processes
            self.log("Checking for running CrossOver processes...")
            try:
                subprocess.run(['pkill', '-f', 'CrossOver'], check=False, 
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.log("CrossOver processes terminated (if any were running)")
            except Exception as e:
                self.log(f"Note: Could not terminate CrossOver processes: {e}")
            
            # Wait for processes to terminate
            time.sleep(2)
            
            # Step 2: Reset FirstRunDate
            self.log("Resetting CrossOver FirstRunDate...")
            user_path = os.path.expanduser('~')
            plist_path = f'{user_path}/Library/Preferences/com.codeweavers.CrossOver.plist'
            
            try:
                with open(plist_path, 'rb') as f:
                    pl = plistlib.load(f)
                
                pl['FirstRunDate'] = datetime.now()
                
                with open(plist_path, 'wb') as f:
                    plistlib.dump(pl, f)
                
                self.log("✓ FirstRunDate reset successfully!")
            except FileNotFoundError:
                self.log("CrossOver preferences file not found.", error=True)
                self.log("Make sure CrossOver is installed and has been run at least once.", error=True)
                self.finish_reset(success=False)
                return
            except Exception as e:
                self.log(f"Error resetting FirstRunDate: {e}", error=True)
                self.finish_reset(success=False)
                return
            
            # Step 3: Reset bottles
            self.log("\nResetting CrossOver bottles...")
            bottles_path = os.path.expanduser("~/Library/Application Support/CrossOver/Bottles/")
            
            if not os.path.exists(bottles_path):
                self.log("No bottles directory found. Skipping bottle reset.")
                self.finish_reset(success=True)
                return
            
            bottles = [f.name for f in os.scandir(bottles_path) if f.is_dir()]
            
            if not bottles:
                self.log("No bottles found. Skipping bottle reset.")
                self.finish_reset(success=True)
                return
            
            self.log(f"Found {len(bottles)} bottle(s) to process...")
            
            bottles_processed = 0
            for bottle in bottles:
                self.log(f"\n→ Processing bottle: {bottle}")
                regfile = os.path.expanduser(
                    f"~/Library/Application Support/CrossOver/Bottles/{bottle}/system.reg"
                )
                
                if not os.path.exists(regfile):
                    self.log(f"  Registry file not found for {bottle}. Skipping.")
                    continue
                
                try:
                    # Compile the regex pattern
                    pattern = re.compile(r"\[Software\\\\CodeWeavers\\\\CrossOver\\\\cxoffice\] [0-9]*")
                    
                    # Read the file
                    with open(regfile, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                    
                    # Search for match
                    match_line_num = None
                    for i, line in enumerate(lines):
                        if pattern.search(line):
                            match_line_num = i
                            break
                    
                    if match_line_num is not None:
                        self.log(f"  Match found at line {match_line_num + 1}")
                        
                        # Delete the trial tracking lines (5 lines total)
                        new_lines = lines[:match_line_num] + lines[match_line_num + 5:]
                        
                        with open(regfile, 'w', encoding='utf-8') as f:
                            f.writelines(new_lines)
                        
                        self.log(f"  ✓ Trial tracking removed from {bottle}")
                        bottles_processed += 1
                    else:
                        self.log(f"  No trial tracking found in {bottle}")
                
                except Exception as e:
                    self.log(f"  Error processing {bottle}: {e}", error=True)
                    continue
            
            if bottles_processed > 0:
                self.log(f"\n✓ Successfully processed {bottles_processed} bottle(s)!")
            
            self.finish_reset(success=True)
            
        except Exception as e:
            self.log(f"\nUnexpected error: {e}", error=True)
            self.finish_reset(success=False)
    
    def finish_reset(self, success=True):
        """Clean up after reset"""
        self.progress.stop()
        self.reset_button.config(state=tk.NORMAL)
        
        if success:
            self.log("\n" + "="*50)
            self.log("CrossOver trial reset complete!")
            self.log("You can now open CrossOver with a fresh trial.")
            self.log("="*50)
            
            # Show success dialog
            self.root.after(100, lambda: messagebox.showinfo(
                "Success",
                "CrossOver trial has been reset successfully!\n\nYou can now open CrossOver."
            ))
        else:
            self.log("\n" + "="*50)
            self.log("Reset process completed with errors.")
            self.log("Please check the messages above for details.")
            self.log("="*50)
            
            # Show error dialog
            self.root.after(100, lambda: messagebox.showerror(
                "Error",
                "Reset process encountered errors.\n\nPlease check the status log for details."
            ))


def main():
    # Create the main window
    root = tk.Tk()
    
    # Set Mac-specific styling
    try:
        style = ttk.Style()
        style.theme_use('aqua')  # Use macOS native theme
    except:
        pass
    
    # Create the app
    app = CrossOverResetApp(root)
    
    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
