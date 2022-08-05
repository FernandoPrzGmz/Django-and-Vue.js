DJANGO = python manage.py

#: > help
#: 	Muestra una lista de las opciones disponibles junto con una breve descripción
#:
.PHONY: help
help:
	@egrep -o "^#: (.+)" [Mm]akefile  | sed 's/#: / /'


#: > demo
#: 	Instalacion del proyecto demo
#:
.PHONY: demo
demo:
	find . -path "*.sqlite3" -delete
	$(DJANGO) migrate
	$(DJANGO) loaddata $(shell pwd)/.db_fixtures/*.json
	$(DJANGO) createsuperuser --username pycun --email pycun@pycun.net


#: > docs
#: 	Contruye la documentacion del proyecto
#:
.PHONY: docs
docs:
	find ./docs/ -type d -name "_build" -exec rm -rf {} +
	/bin/sh -c "cd ./docs; make html"
