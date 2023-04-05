## I beg your pardon?
[Transmogrify](https://www.merriam-webster.com/dictionary/transmogrify) as a repository name? 🔊 trans-mo-gri-fiii? 

> Seems esoteric, good enough. 

How can I reduce laborious tasks to improving productivity?

There's something fun to be made for the heck of it.

### TLDR 
Exploring what I can do with OpenAI.

### 🫧

Create `.env` file to store OpenAI API Key.

```bash
touch .env
```

Create a virtual environment (venv) and initiate. 

```bash
python -m venv

# python3 also works

venv/bin/activate
```

Use `deactivate` to exit venv.

Install package requirements

```bash
pip install -r requirements.txt
```

Start the web application. `--host=127.0.0.1` are `--port=5000` are default. Use `netstat -tulpn` to see port and address in use.

```bash
# initiates web app with all defaults
flask run
# e.g. flask run --host=127.0.5.3 --port=5006
```

Run app as `__main__` to expose to app to the network.

```bash
python app.py
```

Sample `.env` file:

```txt
FLASK_APP=app
FLASK_ENV=development

OPENAI_API_KEY=
```

#### References

Adapted from the [Quickstart guide](https://github.com/openai/openai-quickstart-python)

