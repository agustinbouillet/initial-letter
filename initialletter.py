from PIL import Image, ImageDraw, ImageFont


class InitialLetter():
    def __init__(self, **kwargs):
        self.fontfamilyfile = kwargs['fontfamilyfile'] if 'fontfamilyfile' in kwargs  else ""
        self.filename = kwargs['filename'] if 'filename' in kwargs  else "initialletter"
        self.fontsize = kwargs['fontsize'] if 'fontsize' in kwargs else 65
        self.canvassize = kwargs['canvassize'] if 'canvassize' in kwargs else (120, 120)
        self.quality = kwargs['quality'] if 'quality' in kwargs else 100
        self.filepath = kwargs['filepath'] if 'filepath' in kwargs else ''
        self.text = kwargs['text'] if 'text' in kwargs else 'A'
        self.color = self.hextorgb(kwargs['color']) if 'color' in kwargs else '(255,255,255)'
        self.background = self.hextorgb(kwargs['background']) if 'background' in kwargs else '(125,125,125)'

    def create(self):
        """
        Crea una imagen
        :return: void
        """
        txt = self.text
        image = Image.new("RGBA", self.canvassize, self.background)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(self.fontfamilyfile, self.fontsize)
        text_size = draw.textsize(txt, font=font)

        x = (self.canvassize[0] / 2) - (text_size[0] / 2)
        y = (self.canvassize[1] / 2) - (text_size[1] / 2)
        draw.text((x, y), txt, self.color, font=font)
        image.resize(self.canvassize, Image.ANTIALIAS)
        image.save('%s%s.jpg' % (self.filepath, self.filename), "JPEG", quality=self.quality)

    def hextorgb(self, value):
        """
        Pasa un color expresado con valores hexadecimales a RGB.
        :param value: string Valor hexadecimal
        :return: tuple, Color en RGB
        """
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
