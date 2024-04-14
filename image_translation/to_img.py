from PIL import Image, ImageDraw
import math

CHARS = '@#MBHA$Gh93X25Sisr;:,.'
SCALE_FACTOR = 0.1
ONE_CHAR_WIDTH = 7
ONE_CHAR_HEIGHT = 14


class ImageConverter:
    def __init__(self, input_image):
        self.charArray = list(CHARS)
        self.charLength = len(self.charArray)
        self.interval = self.charLength / 256
        self.scaleFactor = SCALE_FACTOR
        self.oneCharWidth = ONE_CHAR_WIDTH
        self.oneCharHeight = ONE_CHAR_HEIGHT
        self.input_image = Image.open(input_image)

    def get_char(self, input_int):
        return self.charArray[math.floor(input_int * self.interval)]

    def convert_image(self):
        im = self.input_image

        width, height = im.size
        im = im.resize((int(self.scaleFactor * width),
                        int(self.scaleFactor * height
                            * (self.oneCharWidth / self.oneCharHeight))),
                       Image.NEAREST)

        width, height = im.size
        pix = im.load()

        outputImage = Image.new('RGB',
                                (self.oneCharWidth * width,
                                 self.oneCharHeight * height),
                                color=(0, 0, 0))
        d = ImageDraw.Draw(outputImage)

        for i in range(height):
            for j in range(width):
                r, g, b = pix[j, i]

                h = 0.3 * r + 0.59 * g + 0.11 * b

                text = self.get_char(h)
                d.text((j * self.oneCharWidth,
                        i * self.oneCharHeight),
                       text,
                       fill=(r, g, b))

        return outputImage
