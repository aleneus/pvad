all: help

help:
	@echo "make view path=path_to_md_file.md"

view:
	pandoc -s -o $(path).html --css=style.css $(path)
