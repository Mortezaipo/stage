default: stage

stage: stage
	~/.venv/py3/bin/python src/stage.py

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete

check:
	echo "pass"

check-config:
	echo "pass"

get-deps:
	echo "pass"