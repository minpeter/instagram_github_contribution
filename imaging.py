from PIL import Image, ImageDraw, ImageColor, ImageFont

fontPath = "D2Coding.ttf"
W, H = (1080,1080)
bkColor = "#22212C"
fontColor = "#FFFFE0"
sans16  =  ImageFont.truetype ( fontPath, 50)


def imageMaker(msg):
    im = Image.new("RGB", (W,H), ImageColor.getrgb(bkColor))
    draw = ImageDraw.Draw(im)
   # w, h = draw.textsize(msg)

    draw.text((10,10), msg, font=sans16, fill=ImageColor.getrgb(fontColor))

    im.save("code.png", "PNG")