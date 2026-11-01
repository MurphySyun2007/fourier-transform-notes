MAIN  = main
TEX   = $(MAIN).tex ch1.tex ch2.tex ch3.tex ch4.tex ch5.tex ch6.tex appA.tex appB.tex

all: $(MAIN).pdf

$(MAIN).pdf: $(TEX)
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(MAIN).tex

quick: $(TEX)
	pdflatex -interaction=nonstopmode $(MAIN).tex

clean:
	latexmk -c

distclean:
	latexmk -C

.PHONY: all quick clean distclean
