import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from settings import development

from Navigator import app

if __name__ == "__main__":
    app.run()
