import imquality.brisque as brisque
import PIL.Image

from typing import AnyStr


def score_image(image_path: AnyStr) -> float:
    img = PIL.Image.open(image_path)
    return brisque.score(img)
