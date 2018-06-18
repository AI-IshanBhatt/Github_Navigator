# -*- coding: utf-8 -*-

from flask import Flask
from settings import development
import logging

app = Flask(__name__)
app.config.from_object(development)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.INFO)

# print(app.__dict__)

import Navigator.routes
