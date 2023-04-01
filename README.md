## I beg your pardon?
[Transmogrify](https://www.merriam-webster.com/dictionary/transmogrify) as a repository name? 🔊 trans-mo-gri-fiii? 

> Seems esoteric, good enough. 

How can I reduce laborious tasks to improving productivity?

There's something fun to be made for the heck of it.

### TLDR 
Exploring what I can do with Openai.

### 🫧

```bash
# create .env file to store OpenAI API Key

$ touch .env

# create virtual envirornment and initiate 

$ python3 -m venv
$ . venv/bin/activate

# `deactivate` to exit venv

# install package requirements

$ pip install -r requirements.txt

# start the web application

$ flask run

```

Sample `.env` file:

```txt
FLASK_APP=app
FLASK_ENV=development

OPENAI_API_KEY=
```

#### References

Adapted from the [Quickstart guide](https://github.com/openai/openai-quickstart-python)

