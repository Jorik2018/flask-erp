https://python-poetry.org/docs/managing-environments/
https://realpython.com/intro-to-pyenv/
https://github.com/jsonpickle/jsonpickle
poetry env use python3.11
pyenv exec poetry add dependency-injector
poetry add flask --verbose
poetry build
poetry install
poetry run flask --app flask_erp/app.py run