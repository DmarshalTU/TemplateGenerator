import logging
from flask import Flask
from flask import request
from flask import session

from src.clone_temp import clone_template
from src.pattern_replace import pattern_replace
from src.upload_new import upload_new


logging.basicConfig(filename="app.log", filemode="w", level=logging.INFO)


app = Flask(__name__)


logging.info("starting app")
app.add_url_rule("/api/v1/", endpoint="index", methods=["GET"])
app.add_url_rule("/api/v1/templates/", endpoint="templates", methods=["GET"])
app.add_url_rule("/api/v1/template/", endpoint="get_template", methods=["POST"])


@app.endpoint("index")
def index():
    app.logger.debug(session.get)
    return """<h1>Use http://127.0.0.1:5000/api/v1/template/test-project</h1>"""


@app.endpoint("templates")
def templates():
    app.logger.debug(session.get)
    return "repo list"


@app.endpoint("get_template")
def get_template():
    app.logger.debug(session.get)
    data = request.get_json()

    git_repo = data["git_repo"]
    conf_dir = data["conf_dir"]
    new_project = data["new_project"]

    if clone_template(git_repo, new_project) is True:
        pattern_replace(new_project, conf_dir)
        upload_new(new_project)
        return f"git@gitlab-ber1.cyren.io:dataservices/template-playground/{new_project}.git"

    return "Template not cloned"


if __name__ == "__main__":
    app.run(debug=False)
