import logging

from PIL import Image, ImageDraw, ImageFont


class ImageEditor:
    @staticmethod
    def draw(path: str, text: str, fontsize: int):
        image = Image.open(path)
        font = ImageFont.truetype('Impact Regular.ttf', fontsize)
        drawer = ImageDraw.Draw(image)
        size = image.size
        drawer.text((size[0] / 2, size[1] - size[1] / 3), text=text,
                    font=font, fill='white', anchor='mm')
        image.save(path)
        logging.info(f'Image successfully saved to {path}')