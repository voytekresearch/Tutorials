.PHONY: help book clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  book    to convert the `notebooks/` folder into Jekyll markdown in `chapters/`"
	@echo "  clean       to clean out site build files"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"
	@echo "  serve       to serve the repository locally with Jekyll"

textbook:
	python scripts/clean.py

	rm -rf content

	git clone -b dev --single-branch --depth 1 https://github.com/voytekresearch/tutorials content
	rm content/README.md

	python scripts/generate_book.py

	rm -rf content

runall:
	python scripts/execute_all_notebooks.py

clean:
	python scripts/clean.py

serve:
	bundle exec guard
