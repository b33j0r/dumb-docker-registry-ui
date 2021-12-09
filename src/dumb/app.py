from flask import Flask, redirect

from dumb.browse import browse
from dumb.config import get_config

app = Flask(__name__)
app.register_blueprint(browse)

config = get_config()


@app.route("/")
def get_app_root():
    return redirect("browse.get_catalog")


def main(host="0.0.0.0", port=5858):
    app.run(host=host, port=int(port), debug=True)


if __name__ == "__main__":
    main()
