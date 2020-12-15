#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import request
from flask import make_response, jsonify, request
from image_score import score_image
import requests
import oss2
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARNING)

@app.route('/', methods=['GET'])
def home():
    image_path = request.args.get("url")
    assert image_path, "image_path falsy"
    score = score_image(image_path)
    logger.info("Score: %s, %s", image_path, score)
    return jsonify(score=score)


def handler(environ, start_response):
    return app(environ, start_response)
