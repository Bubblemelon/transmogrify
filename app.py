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
            temperature=0.6, # degree of randomness for output
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

@app.route('/chat', methods=("GET", "POST"))
def chat(): {}
    


@app.route('/test', methods=['POST'])
def test():

    # if test.validate_on_submit():
    #     ...  # handle the register form
    # # render the same template to pass the error message
    # # or pass `form.errors` with `flash()` or `session` then redirect to /

    test1 = [('Pixie Dust', 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-YgNABaC2IK9apU936paO5HDZ/user-XoPOH165ivwdiHtQ88wma1At/img-CQo7IDWWvnhvzLjvMTCl7Diy.png?st=2023-04-22T07%3A45%3A27Z&se=2023-04-22T09%3A45%3A27Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-22T08%3A28%3A50Z&ske=2023-04-23T08%3A28%3A50Z&sks=b&skv=2021-08-06&sig=ZKwp34mGjKcSvXUjDwKob9tYxIHH7Hf%2BTGsDoo4JIu4%3D'), ('Violet Velvet',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            'https://oaidalleapiprodscus.blob.core.windows.net/private/org-YgNABaC2IK9apU936paO5HDZ/user-XoPOH165ivwdiHtQ88wma1At/img-WnzchRSaqM9irKQtYXEuGg1Z.png?st=2023-04-22T07%3A45%3A33Z&se=2023-04-22T09%3A45%3A33Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-22T06%3A52%3A14Z&ske=2023-04-23T06%3A52%3A14Z&sks=b&skv=2021-08-06&sig=mAM/h3OTwiSDjIMRoRYzQoKnD8d8kKAAciHjpRkFy5o%3D'), ('Amethyst Fluff', 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-YgNABaC2IK9apU936paO5HDZ/user-XoPOH165ivwdiHtQ88wma1At/img-EJwXTv6w4xPJNR8hwtEtqx4e.png?st=2023-04-22T07%3A45%3A38Z&se=2023-04-22T09%3A45%3A38Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-22T08%3A29%3A43Z&ske=2023-04-23T08%3A29%3A43Z&sks=b&skv=2021-08-06&sig=waVR3BGqtactSj50afBRtsbrf2wxChtWyHKtqzLrhqw%3D')]
    test2 = [('hello', '1'), ('ello', '2'), ('llo', '3')]
    return render_template('index.html', test_value=test1)


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
