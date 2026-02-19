#!/usr/bin/env python3
"""
Generate simple app icons for the PWA.
Requires Pillow: pip install Pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Please install Pillow: pip3 install Pillow")
    exit(1)

def create_icon(size, filename):
    # Create a gradient background
    img = Image.new('RGB', (size, size), color='#667eea')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple calendar emoji or icon
    # Using a large text emoji
    font_size = int(size * 0.6)
    try:
        # Try to use system font
        font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    text = "📅"
    
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((size - text_width) // 2, (size - text_height) // 2 - bbox[1])
    
    draw.text(position, text, font=font, embedded_color=True)
    
    img.save(filename, 'PNG')
    print(f"Created {filename}")

if __name__ == '__main__':
    create_icon(192, 'icon-192.png')
    create_icon(512, 'icon-512.png')
    print("\nIcons created successfully!")
    print("If the emoji doesn't show properly, you can replace these with custom icons.")
