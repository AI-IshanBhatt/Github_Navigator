from Navigator import app
from flask import request, jsonify
import settings.development as settings
from .utils import get_repositories

#-------------------------------
# Root Routes
#-------------------------------

@app.route('/navigator')
def get_repos(page_size=settings.PAGE_SIZE, order=settings.ORDER):
    search_term = request.args.get('search_term')
    return jsonify(get_repositories(search_term, page_size, order))

@app.route('/')
def index():
    return "Hello World"
