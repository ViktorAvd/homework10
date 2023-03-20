from flask import Flask
from utils import load_candidates

app = Flask(__name__)

candidates = load_candidates()


@app.route("/")
def page_index():
    str_ = '<pre>'
    for candidate in candidates.values():
        str_ += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
    str_ += '</pre>'
    return str_


@app.route("/candidates/<int:pk>")
def profile(pk):
    candidate = f"<img src={candidates[pk]['picture']}><br><pre>{candidates[pk]['name']}<br>" \
                f"{candidates[pk]['position']}<br>{candidates[pk]['skills']}<br><br></pre>"
    return candidate


@app.route("/skills/<skill>")
def search_skill(skill):
    total = "<pre>"

    for candidate in candidates.values():
        candidates_skills = candidate["skills"].split(", ")
        candidates_skills = [x.lower() for x in candidates_skills]
        if skill in candidates_skills:
            total += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n"
            continue
    total += "</pre>"

    return total


app.run()
