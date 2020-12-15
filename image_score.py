import imquality.brisque as brisque
from PIL import Image
import requests
from typing import AnyStr
import logging

logger = logging.getLogger()     

def score_image(image_path: AnyStr) -> float:
    is_url = image_path.lower().startswith("http")
    logger.info("is url?", is_url, image_path)
    if is_url:
        r = requests.get(image_path, stream=True)
        r.raw.decode_content = True  # Content-Encoding
        img = Image.open(r.raw)
    else:
        img = Image.open(image_path)
    return brisque.score(img)
