.PHONY: all
all: readme.html todo.html

readme.html : readme.rst
	rst2html readme.rst readme.html

todo.html : todo.md
	markdown todo.md > todo.html

.PHONY: validate
validate:
	./validate_equajson.py -s schema.json json/
