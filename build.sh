mkdir -p tikz/resource
xelatex -shell-escape astro-notebook.tex
bibtex astro-notebook
xelatex -shell-escape astro-notebook.tex
