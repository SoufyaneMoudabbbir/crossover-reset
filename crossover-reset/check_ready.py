#!/usr/bin/env python3
"""
Pre-flight check script
Verifies that all requirements are met before building the Mac app
"""

import sys
import subprocess
import os
from pathlib import Path

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def check(description, test_func):
    """Run a check and print result"""
    print(f"Checking {description}...", end=" ")
    try:
        result, message = test_func()
        if result:
            print(f"{GREEN}✓{RESET} {message}")
            return True
        else:
            print(f"{RED}✗{RESET} {message}")
            return False
    except Exception as e:
        print(f"{RED}✗{RESET} Error: {e}")
        return False

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    return False, f"Python {version.major}.{version.minor} (need 3.8+)"

def check_tkinter():
    """Check if tkinter is available"""
    try:
        import tkinter
        return True, "tkinter available"
    except ImportError:
        return False, "tkinter not available (install python3-tk)"

def check_xcode_tools():
    """Check if Xcode command line tools are installed"""
    try:
        result = subprocess.run(
            ['xcode-select', '-p'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return True, "Xcode tools installed"
        return False, "Xcode tools not installed"
    except FileNotFoundError:
        return False, "xcode-select not found"

def check_py2app():
    """Check if py2app is installed"""
    try:
        import py2app
        return True, "py2app installed"
    except ImportError:
        return False, "py2app not installed (pip3 install py2app)"

def check_pyinstaller():
    """Check if PyInstaller is installed"""
    try:
        result = subprocess.run(
            ['pyinstaller', '--version'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            return True, f"PyInstaller {version}"
        return False, "PyInstaller not working"
    except FileNotFoundError:
        return False, "PyInstaller not installed (pip3 install pyinstaller)"

def check_required_files():
    """Check if required files exist"""
    required = [
        'crossover_reset_gui.py',
        'setup.py',
        'build.sh'
    ]
    missing = [f for f in required if not Path(f).exists()]
    if not missing:
        return True, "All required files present"
    return False, f"Missing files: {', '.join(missing)}"

def check_icon():
    """Check if icon file exists (optional)"""
    if Path('icon.icns').exists():
        size = Path('icon.icns').stat().st_size / 1024
        return True, f"icon.icns found ({size:.1f} KB)"
    return True, "icon.icns not found (optional)"

def main():
    print(f"\n{BLUE}{'='*50}{RESET}")
    print(f"{BLUE}CrossOver Reset - Pre-flight Check{RESET}")
    print(f"{BLUE}{'='*50}{RESET}\n")
    
    checks = [
        ("Python version", check_python_version),
        ("tkinter library", check_tkinter),
        ("Xcode Command Line Tools", check_xcode_tools),
        ("py2app", check_py2app),
        ("PyInstaller", check_pyinstaller),
        ("Required files", check_required_files),
        ("App icon", check_icon),
    ]
    
    results = []
    for description, check_func in checks:
        results.append(check(description, check_func))
    
    print(f"\n{BLUE}{'='*50}{RESET}")
    
    required_checks = results[:6]  # First 6 are required
    critical_passed = all(results[:4])  # Python, tkinter, Xcode, required files
    build_tool_available = results[3] or results[4]  # py2app or PyInstaller
    
    if critical_passed and build_tool_available:
        print(f"{GREEN}✓ Ready to build!{RESET}\n")
        print("Next steps:")
        print(f"  1. Run: {YELLOW}./build.sh{RESET}")
        print(f"  2. Or manually: {YELLOW}python3 setup.py py2app{RESET}")
        print(f"  3. Or with PyInstaller: {YELLOW}pyinstaller --windowed --onefile crossover_reset_gui.py{RESET}\n")
        return 0
    else:
        print(f"{RED}✗ Not ready to build{RESET}\n")
        print("Please fix the issues above before building.")
        print("\nQuick fixes:")
        
        if not results[0]:  # Python version
            print(f"  • Install Python 3.8+: {YELLOW}https://www.python.org{RESET}")
        
        if not results[1]:  # tkinter
            print(f"  • Install tkinter: {YELLOW}brew install python-tk@3.11{RESET}")
        
        if not results[2]:  # Xcode tools
            print(f"  • Install Xcode tools: {YELLOW}xcode-select --install{RESET}")
        
        if not results[3] and not results[4]:  # Neither build tool
            print(f"  • Install py2app: {YELLOW}pip3 install py2app{RESET}")
            print(f"  • Or PyInstaller: {YELLOW}pip3 install pyinstaller{RESET}")
        
        print()
        return 1

if __name__ == "__main__":
    sys.exit(main())
