from PIL import Image, ImageDraw, ImageFont
import numpy as np

def get_average_color(image):
    """Compute average RGB color of an image. to dissuade situations where contrast is high and editing is easy"""
    np_image = np.array(image)
    if len(np_image.shape) == 3:
        mean = np_image.mean(axis=(0, 1))[:3]
        return tuple(map(int, mean))
    else:
        return (0, 0, 0)

def add_watermark(input_path: str, text: str, _spacing: int = 1):
    # Output Paths
    base_name = input_path.split(".")[0]
    output_path = base_name+"-watermarked.png"
    image = Image.open(input_path).convert("RGB")
    
    # Font color to use
    r,g,b = (128,128,128) #get_average_color(image)

    # Create watermark layer
    spacing = _spacing*100
    expanded_size = (image.size[0]+8*spacing, image.size[1]+8*spacing) # expand the size since the image will be rotated 45 degrees, if we didn't expand then the corners will be clipped (not filled with watermark)

    watermark = Image.new("RGBA", expanded_size, (255,255,255,0))
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(watermark)

    fill = (r, g, b, 128)  # Add some transparency

    # The ff draws the text in the expanded canvas
    for y in range(-expanded_size[1], expanded_size[1], spacing*0.8):
        for x in range(-expanded_size[0], expanded_size[0], spacing*1.2):
            draw.text((x, y), text, fill=fill, font=font, )

    # rotate the expanded watermark canvas by 45 degrees and then crop the middle part to ensure the whole image gets covered with the watermark
    watermark = watermark.rotate(45, expand=1)
    watermark = watermark.crop((spacing*4, spacing*4, image.size[0]+spacing*4, image.size[1]+spacing*4))

    result = Image.alpha_composite(image.convert("RGBA"), watermark)
    result.save(output_path)


add_watermark("input.jpg", "FOR LTMS\nACCOUNT RECOVERY")
