# Resume

This project uses a Makefile for compiling LaTeX documents into PDF and Markdown formats while allowing for the inclusion of sensitive personal data through environment variables.

## Features

- **Build PDF:** Compiles the LaTeX resume document into a PDF, using personal contact information specified in local environment variables.
- **Development Watch Mode:** Starts a process to watch for any changes in LaTeX files and recompiles the PDF for local development purposes.
- **Markdown Conversion:** Converts the LaTeX document to a Markdown file, excluding the header section.

## Usage

To use these features, you should have a `.env` file with the following content:

```plaintext
PHONE=your_actual_phone_number
EMAIL=your_actual_email_address
```

Replace `your_actual_phone_number` and `your_actual_email_address` with your personal contact information. This data is used when building resumes for personal distribution.

### Commands

- `make` or `make resume`: Compiles the LaTeX resume to PDF using the provided phone and email from the `.env` file.
- `make watch`: Watches for changes in the LaTeX files and recompiles when changes are detected.
- `make markdown`: Generates a Markdown version of the LaTeX resume.
- `make clean`: Cleans up auxiliary files generated by LaTeX during compilation.

## Dependencies

- LaTeX distribution (e.g., TeX Live, MiKTeX, etc.) for PDF compilation.
- `pdflatex` command for LaTeX processing.
- `pandoc` and a custom `remove_header.py` script for Markdown conversion.
- `entr` utility to automate the recompilation when files change.
- `zathura` PDF viewer for viewing the PDF output in watch mode (optional).

Ensure all dependencies are installed on your system to utilize this Makefile's full capabilities.

## Notes

- The `.env` file is not tracked by version control to keep personal data secure.
- The `make watch` command requires the `entr` command to be installed and will open the resulting PDF in `zathura` if it is not already open.

Please replace the placeholder values in the `.env` sample with your actual information before using the Makefile to build your resume. If not present the documents generated will omit these details.
