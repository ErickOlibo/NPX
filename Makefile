run:
	python src/app/main.py

install: requirements.txt
	pip install -r requirements.txt

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist