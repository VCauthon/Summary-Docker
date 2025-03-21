from flask import render_template, Blueprint


bp = Blueprint("main", __name__)


@bp.route("/")
def main():
    return render_template("index.html")