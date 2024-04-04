all:build clean

clean:
	rm -f main.aux
	rm -f main.log
	rm -f main.toc

build:
	pdflatex main.tex
	pdflatex main.tex
	pdflatex main.tex