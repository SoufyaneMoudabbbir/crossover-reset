#!/bin/bash
# Automated build script for CrossOver Reset Mac app
# This script handles the entire build process automatically

set -e  # Exit on error

echo "=================================="
echo "CrossOver Reset - App Builder"
echo "=================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python 3 is installed
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    echo "Please install Python 3 from https://www.python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✓ Found Python $PYTHON_VERSION${NC}"
echo ""

# Ask which method to use
echo "Choose build method:"
echo "1) py2app (Recommended - better integration)"
echo "2) PyInstaller (Alternative - faster builds)"
read -p "Enter choice (1 or 2): " choice
echo ""

if [ "$choice" == "1" ]; then
    BUILD_METHOD="py2app"
elif [ "$choice" == "2" ]; then
    BUILD_METHOD="pyinstaller"
else
    echo -e "${RED}Invalid choice${NC}"
    exit 1
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist *.spec
echo -e "${GREEN}✓ Cleaned${NC}"
echo ""

# Install/upgrade build tool
echo "Installing/upgrading $BUILD_METHOD..."
if [ "$BUILD_METHOD" == "py2app" ]; then
    pip3 install --upgrade py2app --quiet
else
    pip3 install --upgrade pyinstaller --quiet
fi
echo -e "${GREEN}✓ $BUILD_METHOD ready${NC}"
echo ""

# Build the app
echo "Building CrossOver Reset.app..."
echo "This may take a few minutes..."
echo ""

if [ "$BUILD_METHOD" == "py2app" ]; then
    python3 setup.py py2app
else
    # Check if icon exists
    ICON_ARG=""
    if [ -f "icon.icns" ]; then
        ICON_ARG="--icon=icon.icns"
    fi
    
    pyinstaller --name="CrossOver Reset" \
                --windowed \
                --onefile \
                --osx-bundle-identifier=com.crossover.reset \
                $ICON_ARG \
                --clean \
                --noconfirm \
                crossover_reset_gui.py
fi

echo ""
echo -e "${GREEN}✓ Build complete!${NC}"
echo ""

# Check if app was created
if [ -d "dist/CrossOver Reset.app" ]; then
    APP_SIZE=$(du -sh "dist/CrossOver Reset.app" | cut -f1)
    echo -e "${GREEN}Success! App created:${NC}"
    echo "  Location: dist/CrossOver Reset.app"
    echo "  Size: $APP_SIZE"
    echo ""
    
    # Ask if user wants to test
    read -p "Do you want to test the app now? (y/n): " test_choice
    if [ "$test_choice" == "y" ] || [ "$test_choice" == "Y" ]; then
        echo "Opening app..."
        open "dist/CrossOver Reset.app"
    fi
    
    echo ""
    echo "=================================="
    echo "Next Steps:"
    echo "=================================="
    echo "1. Test the app: open 'dist/CrossOver Reset.app'"
    echo "2. Package for distribution:"
    echo "   cd dist"
    echo "   zip -r 'CrossOver Reset.app.zip' 'CrossOver Reset.app'"
    echo "3. Upload to GitHub releases"
    echo ""
    echo "To remove code signature warnings on other Macs:"
    echo "   xattr -cr 'CrossOver Reset.app'"
    echo ""
    
else
    echo -e "${RED}Error: App was not created${NC}"
    echo "Check the output above for errors"
    exit 1
fi
