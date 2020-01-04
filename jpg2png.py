from PIL import Image  # Python Image Library
import glob

for file in glob.glob("*.jpg"):
    im = Image.open(file)
    rgb_im = im.convert("RGB")
    rgb_im.save(file.replace("jpg", "png"), optimize=True)
