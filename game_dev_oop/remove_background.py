from PIL import Image
import math

img = Image.open("starter/assets/coin.jpg").convert("RGBA")

datas = img.getdata()
newData = []
for r, g, b, a in datas:
    if (
        math.sqrt((255 - r) ** 2 + (255 - g) ** 2 + (255 - b) ** 2) < 60
    ):  # adjust threshold here
        newData.append((255, 255, 255, 0))
    else:
        newData.append((r, g, b, a))

img.putdata(newData)
img.save("starter/assets/coin.png", "PNG")
