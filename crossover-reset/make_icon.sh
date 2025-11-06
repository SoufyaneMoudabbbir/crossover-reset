#!/bin/bash
# Icon Generator for Mac App
# This script converts a PNG image to .icns format

echo "=================================="
echo "Mac App Icon Generator"
echo "=================================="
echo ""

# Check if a PNG file was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./make_icon.sh <image.png>"
    echo ""
    echo "Example: ./make_icon.sh my_icon.png"
    echo ""
    echo "Requirements:"
    echo "  - PNG image (1024x1024 recommended)"
    echo "  - macOS sips and iconutil (built-in)"
    exit 1
fi

INPUT_FILE="$1"

# Check if file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File '$INPUT_FILE' not found"
    exit 1
fi

# Check if it's a PNG
if [[ "$INPUT_FILE" != *.png ]]; then
    echo "Error: Input file must be a PNG image"
    exit 1
fi

echo "Input: $INPUT_FILE"
echo ""

# Create iconset directory
ICONSET_DIR="icon.iconset"
rm -rf "$ICONSET_DIR"
mkdir "$ICONSET_DIR"

echo "Generating icon sizes..."

# Generate all required sizes
sips -z 16 16     "$INPUT_FILE" --out "$ICONSET_DIR/icon_16x16.png" > /dev/null 2>&1
sips -z 32 32     "$INPUT_FILE" --out "$ICONSET_DIR/icon_16x16@2x.png" > /dev/null 2>&1
sips -z 32 32     "$INPUT_FILE" --out "$ICONSET_DIR/icon_32x32.png" > /dev/null 2>&1
sips -z 64 64     "$INPUT_FILE" --out "$ICONSET_DIR/icon_32x32@2x.png" > /dev/null 2>&1
sips -z 128 128   "$INPUT_FILE" --out "$ICONSET_DIR/icon_128x128.png" > /dev/null 2>&1
sips -z 256 256   "$INPUT_FILE" --out "$ICONSET_DIR/icon_128x128@2x.png" > /dev/null 2>&1
sips -z 256 256   "$INPUT_FILE" --out "$ICONSET_DIR/icon_256x256.png" > /dev/null 2>&1
sips -z 512 512   "$INPUT_FILE" --out "$ICONSET_DIR/icon_256x256@2x.png" > /dev/null 2>&1
sips -z 512 512   "$INPUT_FILE" --out "$ICONSET_DIR/icon_512x512.png" > /dev/null 2>&1
sips -z 1024 1024 "$INPUT_FILE" --out "$ICONSET_DIR/icon_512x512@2x.png" > /dev/null 2>&1

echo "✓ All sizes generated"
echo ""

# Convert to .icns
echo "Creating icon.icns..."
iconutil -c icns "$ICONSET_DIR" > /dev/null 2>&1

if [ -f "icon.icns" ]; then
    echo "✓ icon.icns created successfully!"
    
    # Show file size
    SIZE=$(du -sh icon.icns | cut -f1)
    echo ""
    echo "Output: icon.icns ($SIZE)"
    
    # Clean up
    rm -rf "$ICONSET_DIR"
    echo "✓ Cleaned up temporary files"
    echo ""
    echo "You can now use icon.icns in your app build!"
else
    echo "Error: Failed to create icon.icns"
    exit 1
fi
