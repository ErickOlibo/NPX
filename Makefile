.PHONY: run clean

# create and setup the virtual environment
venv/bin/activate: requirements.txt
	python -m venv .venv
	. .venv/Scripts/activate; \
	pip install -r requirements.txt

# run the app
run: venv/bin/activate
	. .venv/Scripts/activate; \
	python src/app/main.py

# clean up artifacts from previous builds
clean:
	rm -r src/app/__pycache__
	rm -r .venv
	rm -r .idea