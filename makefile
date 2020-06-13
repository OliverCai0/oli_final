test: t.mdl main.py matrix.py mdl.py display.py draw.py gmath.py
	python main.py t.mdl
	display teapotheist.gif

clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc *out parsetab.py *ppm
