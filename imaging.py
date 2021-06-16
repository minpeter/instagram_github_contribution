from PIL import Image, ImageDraw, ImageColor

W, H = (1080,1080)
color = "#22212C"
msg = """#include <stdio.h>
void main() {
    printf("hello world");
}
"""

im = Image.new("RGB", (W,H), ImageColor.getrgb(color))
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,(H-h)/2), msg, fill="black")

im.save("hello.png", "PNG")