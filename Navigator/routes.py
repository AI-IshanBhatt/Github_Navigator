from Navigator import app
from flask import request, jsonify, render_template, make_response, abort
import settings.development as settings
from .utils import get_repositories

#-------------------------------
# Root Routes
#-------------------------------


@app.route('/navigator')
def get_repos(page_size=settings.PAGE_SIZE, order=settings.ORDER):
    search_term = request.args.get('search_term')
    app.logger.info("Searched for {}".format(search_term))
    # return jsonify(get_repositories(search_term, page_size, order))
    repositories = get_repositories(search_term, page_size, order)
    if repositories:
        return render_template("ReposList.html", repo_list=repositories, search_term=search_term)
    else:
        abort(500)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def resource_unavailable(error):
    return make_response("No Repository with given name", 500)


