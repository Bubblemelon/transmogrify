import os
import sys
import logging

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

        # get string containing names delimited by commas
        # store names as list
        plant_name_list = response.choices[0].text.split(", ")

        tuple_list = []

        for p in plant_name_list:

            # remove leading and trailing white space
            # remove the fullstop in the last element from the list
            pp = p.strip().replace('.', '')

            PROMPT = 'This plant is called, {}, and has these characteristics {}'.format(
                pp, plant)

            respond = openai.Image.create(
                prompt=PROMPT,
                n=1,
                size="256x256",
            )

            # store plant names as element 0th in the tuples
            # store urls as element 1th in the tuples
            #
            # list of tuples ("plant-name", "image-url")
            item = (str(pp), str(respond["data"][0]["url"]))

            tuple_list.append(item)

        return render_template("index.html", result=tuple_list)

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(plant):
    return """Suggest three names that have a supernatural theme for a plant based on the input description.

Plant: Non-flowering
Names: Shadow Tree, Faerie Moss, Serpent's Tongue 
Plant: Flowering
Names: Myrrhical, Mystic Dewdrop, Mermaid's Hair
Plant description: {}
Names:""".format(
        plant.capitalize()
    )


# exposes app to the network when `python app.py` initiates
if __name__ == '__main__':
    print('App is running as main!')
    app.run(debug=False, port=5000, host='0.0.0.0')
