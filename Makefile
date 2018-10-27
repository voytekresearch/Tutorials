.PHONY: help book clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  book    to convert the `notebooks/` folder into Jekyll markdown in `chapters/`"
	@echo "  clean       to clean out site build files"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"
	@echo "  serve       to serve the repository locally with Jekyll"

book:
	python scripts/generate_book.py

runall:
	python scripts/execute_all_notebooks.py

clean:
	python scripts/clean.py

serve:
	#bundle exec guard
	bundle exec jekyll serve

textbook:
	python scripts/clean.py

	rm -rf content/tutorials
	git clone -b dev --single-branch --depth 1 https://github.com/voytekresearch/tutorials content/tutorials
	rm content/tutorials/README.md

	python scripts/generate_book.py

	rm -rf content/tutorials

	rm -rf notebooks
