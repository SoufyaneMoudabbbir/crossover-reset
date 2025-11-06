#!/usr/bin/env python3
import os
import shutil
import re
import plistlib
import subprocess
from datetime import datetime

print("Checking for running CrossOver processes...")
# Kill any running CrossOver processes
try:
    subprocess.run(['pkill', '-f', 'CrossOver'], check=False)
    print("CrossOver processes terminated (if any were running)")
except:
    print("Note: Could not terminate CrossOver processes")

# Wait a moment for processes to fully terminate
import time
time.sleep(2)

print("Resetting Crossover FirstRunDate...")
# Set os path
userPath = os.path.expanduser('~')

# Open plist
try:
    with open(f'{userPath}/Library/Preferences/com.codeweavers.CrossOver.plist', 'rb') as f:
        pl = plistlib.load(f)

    # Set first run date to current time
    pl['FirstRunDate'] = datetime.now()

    # Save plist
    with open(f'{userPath}/Library/Preferences/com.codeweavers.CrossOver.plist', 'wb') as f:
        plistlib.dump(pl, f)
    
    print("FirstRunDate reset successfully!")
except FileNotFoundError:
    print("CrossOver preferences file not found. Make sure CrossOver is installed and has been run at least once.")
    exit(1)

print("Resetting Crossover bottles...")
# Get all of the bottles in the bottles directory
bottles_path = os.path.expanduser("~/Library/Application Support/CrossOver/Bottles/")

if not os.path.exists(bottles_path):
    print("No bottles directory found. Skipping bottle reset.")
    print("CrossOver trial reset complete!")
    exit(0)

bottles = [f.name for f in os.scandir(bottles_path) if f.is_dir()]

if not bottles:
    print("No bottles found. Skipping bottle reset.")
    print("CrossOver trial reset complete!")
    exit(0)

for bottle in bottles:
    print(f"\nProcessing bottle: {bottle}")
    # Define paths
    regfile = os.path.expanduser(f"~/Library/Application Support/CrossOver/Bottles/{bottle}/system.reg")
    
    if not os.path.exists(regfile):
        print(f"Registry file not found for bottle {bottle}. Skipping.")
        continue
        
    bakfile = regfile + ".bak"

    # Create backup
    shutil.copy2(regfile, bakfile)
    print(f"Backup created: {bakfile}")

    # Compile the regex pattern
    pattern = re.compile(r"\[Software\\\\CodeWeavers\\\\CrossOver\\\\cxoffice\] [0-9]*")

    # Read the file and search for match line
    with open(regfile, 'r') as f:
        lines = f.readlines()

    match_line_num = None
    for i, line in enumerate(lines):
        if pattern.search(line):
            match_line_num = i
            break

    # If match is found
    if match_line_num is not None:
        print(f"Match found at line {match_line_num + 1}.")
        for line in lines[match_line_num:match_line_num + 5]:
            print(line, end='')

        resp = input("Do you want to delete these lines (delete to reset bottle)? (y/n): ").strip().lower()
        if resp == 'y':
            new_lines = lines[:match_line_num] + lines[match_line_num + 5:]
            with open(regfile, 'w') as f:
                f.writelines(new_lines)
            print("Lines deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("No match found in this bottle.")

print("\nCrossOver trial reset complete!")
print("You can now open CrossOver and the trial should be reset.")