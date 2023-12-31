# Makefile for building LaTeX documents with personal data from an environment file.

# Include the .env file if it exists
-include .env

.PHONY: all clean watch resume

RESUME=wesley_florence_resume
TEX_FILES=$(wildcard *.tex)

# Default target builds the resume using environment variables if they exist
all: resume

# Compile the LaTeX document with the environment variables
resume: $(TEX_FILES)
	if [ -n "$(PHONE)" ]; \
	then \
		PHONE_CMD="\def\mobile{${PHONE}}"; \
		EMAIL_CMD="\def\email{${EMAIL}}"; \
		pdflatex -interaction=nonstopmode "$$PHONE_CMD $$EMAIL_CMD \input{$(RESUME).tex}"; \
	else \
		pdflatex -interaction=nonstopmode "\input{$(RESUME).tex}"; \
	fi;

markdown:
	pandoc --filter=remove_header.py -t gfm -o $(RESUME).md $(RESUME).tex

html:
	pandoc --filter=remove_header.py -o $(RESUME).html $(RESUME).tex
	# gsed -i 's/ style="[^"]*"//g; s/ class="[^"]*"//g' $(RESUME).html


# Watch for changes in the .tex files, rebuild as needed, and only open zathura if not already open
watch: resume
	@echo "Watching .tex files for changes... Press Ctrl+C to stop."
	@nohup zathura $(RESUME).pdf > /dev/null 2>&1 &
	@ls $(TEX_FILES) | entr -p make resume

# Clean up auxiliary files generated by LaTeX
clean:
	@rm -f *.aux *.log *.out *.pdf *.fls *.fdb_latexmk *.synctex.gz

