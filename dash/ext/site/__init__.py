from flask import request, render_template
from flask import Blueprint


bp = Blueprint("site", __name__)

def init_app(app):
    app.register_blueprint(bp)

@bp.route("/")
def index():
    return render_template(
        "index.html"
        )
  