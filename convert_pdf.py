#!/usr/bin/env python3

import pdfplumber
import re

def convert_pdf_to_markdown(pdf_path, output_path):
    """Convert PDF to Quarto markdown using pdfplumber"""
    
    markdown_content = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text()
            if text:
                # Clean up the text and convert to markdown
                lines = text.split('\n')
                processed_lines = []
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Convert headings (lines that are all caps or end with colon)
                    if line.isupper() and len(line) > 5:
                        processed_lines.append(f"## {line.title()}\n")
                    elif line.endswith(':') and len(line.split()) <= 5:
                        processed_lines.append(f"### {line}\n")
                    else:
                        processed_lines.append(line)
                
                if processed_lines:
                    markdown_content.extend(processed_lines)
                    markdown_content.append("")  # Add blank line between pages
    
    # Write to output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("---\ntitle: \"Syllabus\"\n---\n\n")
        f.write('\n'.join(markdown_content))
    
    print(f"Successfully converted {pdf_path} to {output_path}")

if __name__ == "__main__":
    pdf_file = "syllabusML_NewRice.pdf"
    output_file = "syllabus.qmd"
    
    convert_pdf_to_markdown(pdf_file, output_file)