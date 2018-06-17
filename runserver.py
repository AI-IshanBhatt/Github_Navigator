import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from settings import development

from Navigator import app

app.run(host="0.0.0.0", threaded=True, use_reloader=False)
