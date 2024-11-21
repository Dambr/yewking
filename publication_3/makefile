TARGET='Vak3'
SRC='publication_3'

all:build_document clean_artifacts

clean:clean_document clean_artifacts

clean_artifacts:
	rm -f $(TARGET).log
	rm -f $(TARGET).aux
	rm -f $(TARGET).toc

clean_document:
	rm -f $(TARGET).pdf

build_document:
	pdflatex -jobname='Vak3' publication_3.tex
	pdflatex -jobname='Vak3' publication_3.tex
	pdflatex -jobname='Vak3' publication_3.tex


