from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS, cross_origin
from rake_new2 import Rake
import os
import sys

if sys.platform.lower() == "win32":
    os.system("color")

app = Flask(__name__)
cors = CORS(app)
app.config["CoRS_HEADERS"] = "Content-Type"


@app.route("/")
@app.route("/index")
@cross_origin()
def index():
    return "welcome to RAKE"


@app.route("/extract", methods=["GET", "POST"])
def extract():
    if request.method == "POST":
        req_body = request.get_json()
        print(req_body)
        res = {"top5Words": None, "keywords": None, "keyword_scores": None}

        rake_obj = Rake(keep_html_tags=req_body["keepHtml"])
        rake_obj.get_keywords_from_raw_text(req_body["text"])

        if req_body["showTop5Words"] == True:
            res["top5Words"] = dict(rake_obj.get_word_freq().most_common(5))

        if req_body["other"] == "kwrd":
            res["keywords"] = list(rake_obj.get_ranked_keywords())
        elif req_body["other"] == "kwrd_score":
            res["keyword_scores"] = list(rake_obj.get_keywords_with_scores())
        elif req_body["other"] == "top5":
            res["top5Words"] = dict(rake_obj.get_word_freq().most_common(5))

        print(res)
        return jsonify(res)

    else:
        return "geterror"


if __name__ == "__main__":
    app.run()
