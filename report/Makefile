FILE=report

all:
	xelatex -shell-escape $(FILE).tex
	biber $(FILE)
	xelatex -shell-escape $(FILE).tex
