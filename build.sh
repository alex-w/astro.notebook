mkdir -p tikz/resource                   # Создать папку tikz/resource, если её нет
xelatex -shell-escape astro-notebook.tex # Собрать проект с помощью xelatex c опцией -shell-escape
bibtex astro-notebook                    # Обработать библиографию с помощью bibtex
xelatex -shell-escape astro-notebook.tex # Повторно собрать проект, чтобы обновилась библиография
