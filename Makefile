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
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	rm -rf __pycache__
	rm -rf venv