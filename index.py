#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import request
from flask import make_response
from image_score import score_image
import oss2
import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resp = make_response('<h1>Home World<h1>', 200)
    return resp


def handler(environ, start_response):
    return app(environ, start_response)
