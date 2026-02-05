from flask import Flask, render_template, send_file
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download")
def download():
    return send_file("C:\Users\Welcome\Desktop\forensics_easy\files\forensics_easy_image (1).png", as_attachment=True)


# Local + Nimbus compatible
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port, debug=True)
