import os
from io import BytesIO
from typing import Iterable, Union
from PIL import Image, ImageDraw, ImageFont as IF
import zlib
import pickle


class TMFRAME:
    data: list[list[int]] = pickle.loads(
        zlib.decompress(
            open(os.path.abspath(__file__+'/../data1'), 'rb').read()))

    def __init__(self, image: Union[Image.Image, str, BytesIO]) -> None:
        self.frame = Image.new('RGBA', (1004, 590))
        self.image = Image.open(image) if isinstance(
            image,
            BytesIO) else (
                image if isinstance(
                    image,
                    Image.Image) else Image.open(image))

    def color(self):
        color = {}
        for x in range(self.image.width):
            for y in range(self.image.height):
                pix = self.image.getpixel((x, y))
                if pix[:3] not in [[0, 0, 0], [255, 255, 255]]:
                    if pix.__str__() not in color:
                        color[pix.__str__()] = 1
                    else:
                        color[pix.__str__()] += 1

        s = sorted(list(color), key=lambda x: color[x])
        return eval(s[0])

    def coloring(self, color: Iterable[int] = []):
        for xi, x in enumerate(self.data):
            for yi, y in enumerate(x):
                self.frame.putpixel((xi, yi), (*color, y))

    def pasting(self):
        musik = Image.open(
            os.path.abspath(__file__+'/../not.png'))\
            .resize((190, 190))\
            .crop((40, 40, 170, 170))
        self.image = self.image.resize(
            (self.frame.width,
                int(self.image.width/self.image.height)*self.frame.height))\
            .convert('RGBA')
        self.image.paste(
            self.frame,
            (0, 0),
            self.frame.convert('RGBA'))
        self.image.paste(
            musik,
            (self.image.width-musik.width-10, 5),
            musik.convert('RGBA'))

    def cut(self, text, max, fontsize):
        font = IF.truetype(
            os.path.abspath(__file__+'/../font/FreeSerifItalic.ttf'),
            size=fontsize)
        if font.getsize(text)[0] < max:
            return text
        else:
            while font.getsize(text)[0] > max:
                text = text[:-1]
            return text+'..'

    def drawing(self, author, text):
        text = self.cut(text, 759, 55)
        author = self.cut(author, 384, 50)
        draw = ImageDraw.Draw(self.image)
        draw.text(
            (50, 480),
            text,
            font=IF.truetype(
                os.path.abspath(__file__+'/../font/FreeSerifItalic.ttf'),
                size=50),
            fill=(0, 0, 0))
        draw.text(
            (20, 370),
            author,
            font=IF.truetype(
                os.path.abspath(__file__+'/../font/FreeSerifItalic.ttf'),
                size=55),
            fill=(0, 0, 0))
