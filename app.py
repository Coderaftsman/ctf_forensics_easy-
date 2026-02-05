from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "files", "forensics_easy_cyber_matrix.png")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download")
def download():
    return send_file(FILE_PATH, as_attachment=True)


# Local + Nimbus compatible
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
