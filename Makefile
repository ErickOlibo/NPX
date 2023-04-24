run:
	python NPX/main.py

install: requirements.txt
	pip install -r requirements.txt

clean:
	if exist "./build" rd /s /q build
	if exist "./dits" rd /s /q dist