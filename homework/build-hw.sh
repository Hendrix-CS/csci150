#!/bin/sh

pandoc -f markdown -t latex -s $1.md > $1.tex && pdflatex $1.tex
