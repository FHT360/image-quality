import imquality.brisque as brisque
from PIL import Image
import requests
from typing import AnyStr
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARNING)

def score_image(image_path: AnyStr) -> float:
    is_url = image_path.lower().startswith("http")
    logger.info("%s is url: %s", image_path, is_url)
    if is_url:
        # see https://stackoverflow.com/questions/22340265/python-download-file-using-requests-directly-to-memory
        r = requests.get(image_path, stream=True)
        logger.info("[%s]: %s", r.status_code, image_path)
        r.raw.decode_content = True  # Content-Encoding
        img = Image.open(r.raw)
    else:
        img = Image.open(image_path)
    return brisque.score(img)
