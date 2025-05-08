from rembg import remove
from PIL import Image
input_path="C:\\Users\\Joshua\\Software-Playground\\Scripts\\standalone\\removebgout.png"
output_path="C:\\Users\\Joshua\\Software-Playground\\Scripts\\standalone\\removebgout2.png"
inputimage=Image.open(input_path)
output=remove(inputimage)
output.save(output_path)
