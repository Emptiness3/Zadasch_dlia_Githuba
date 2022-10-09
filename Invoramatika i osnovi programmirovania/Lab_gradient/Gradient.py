from PIL import Image
import math
imgsize=(650,650)
image = Image.new('RGBA', imgsize)
innerColor = [33,12,123]
for y in range(imgsize[1]):
    for x in range(imgsize[0]):
         distanceToCenter = math.sqrt((x - imgsize[0]/2) ** 2 + (y - imgsize[1]/2) ** 2)
         distanceToCenter = float(distanceToCenter) / (math.sqrt(0.5) * imgsize[0]/2)
         r = distanceToCenter + innerColor[0] * (1 - distanceToCenter)
         g =  distanceToCenter + innerColor[1] * (1 - distanceToCenter)
         b =  distanceToCenter + innerColor[2] * (1 - distanceToCenter)
         image.putpixel((x, y), (int(r), int(g), int(b)))
image.save('result.png')