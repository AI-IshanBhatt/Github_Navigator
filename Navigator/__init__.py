# -*- coding: utf-8 -*-

from flask import Flask
from settings import development

app = Flask(__name__)
app.config.from_object(development)

# print(app.__dict__)

import Navigator.routes
