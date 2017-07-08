help:
	@echo
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  docs       to create documentation files"
	@echo "  clean      to clean garbage left by builds and installation"

clean:
	@echo "Execute cleaning ..."
	@find . -type f -name "*.pyc"|xargs rm

pep8:
	@echo "======================================"
	@echo "= PEP8 verification                  ="
	@echo "======================================"
	@find . -type f -not -path "*./.venv/*" -not -path "*/keromudar/*" -not -path "./manage.py" -name "*.py"|xargs flake8 --ignore=E501
	@echo "PEP8 verification successfully !"


build: clean pep8

environment:
	@echo "creating a environment develop"
	@touch keromudar/settings_dev.py
	@virtualenv .venv
	./.venv/bin/pip install -r requirements-dev.txt

tests:
	@echo "======================================"
	@echo "= Initialize run tests               ="
	@echo "======================================"
	./.venv/bin/python manage.py test

runserver:
	./.venv/bin/python manage.py runserver --settings=keromudar.settings_dev

migrate:
	./.venv/bin/python manage.py makemigrations --settings=keromudar.settings_dev
	./.venv/bin/python manage.py migrate --settings=keromudar.settings_dev
