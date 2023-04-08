import os
import sys

import openai

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        plant = request.form["plant"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(plant),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(plant):
    return """Suggest three names that have a supernatural theme for a plant based on the input description.

Plant: Non-flowering
Names: Shadow Tree, Faerie Moss, Serpent's Tongue 
Plant: Flowering
Names: Myrrhical, Mystic Dewdrop, Mermaid's Hair
Plant: {}
Names:""".format(
        plant.capitalize()
    )


# exposes app to the network when `python app.py` initiates
if __name__ == '__main__':
    print('App is running as main!')
    app.run(debug=False, port=5000, host='0.0.0.0')
