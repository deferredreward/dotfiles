#!/usr/bin/env python3
#
# This script gets a HTML annotations file exported from the Kindle app
# and convert it to markdown.
#
# Instructions:
# 1. Download this script.
# 2. Be sure to have python installed.
# 3. Install python dependencies: pip3 install --user beautifulsoup4
# 4. Run the script: python3 kindle2md YOUR_FILE.html
#
# Copyright (C) 2021 Rafael Cavalcanti - rafaelc.org
# Licensed under GPLv3
#

from bs4 import BeautifulSoup
from pathlib import Path
from os.path import basename, splitext
from sys import argv, exit


script_name = basename(__file__)

if len(argv) != 2:
    print(f'Usage: {script_name} html_file')
    exit(1)

source_name = argv[1]
dest_name = splitext(source_name)[0] + '.md'

source = Path(source_name)
dest = Path(dest_name)

if dest.exists():
    print(f'Destination file "{dest}" already exists.')
    answer = input('Overwrite? [y/n] ')
    if answer.lower().strip() != 'y':
        exit(1)

try:
    file_content = source.read_text(encoding='UTF-8')
except OSError as e:
    print(f'Failed to read file: {e}.')
    exit(1)

soup = BeautifulSoup(file_content, 'html.parser')

try:
    book_title = soup.select_one('.bookTitle').contents[0].strip()
    text_elements = soup.select('.noteText')
    all_text_elements = soup.select('.noteText,.sectionHeading')
    desc_elements = soup.select('.noteHeading')
    authors = soup.select_one('.authors').contents[0].strip() 
    citation = soup.select_one('.citation').contents

    texts = [elem.contents[0].strip() for elem in text_elements]
    all_texts = [elem.contents[0].strip() for elem in all_text_elements]

    # Parse descriptions
    types = []
    pages = []
    for elem in desc_elements:
        desc = ''.join(elem.strings).strip()
        desc_words = desc.split('-')
        the_type = desc_words[0]
        the_page = ' '.join(desc_words[-1:])
        types.append(the_type)
        pages.append(the_page)

except AttributeError as e:
    print(f'Error parsing file: {e}')
    exit(1)

output = f'# {book_title}\n\n'
if len(citation) > 1: 
    citeItems = [str(elem) for elem in citation]
    citeItems[0] = citeItems[0].lstrip()
    citeItems[-1] = citeItems[0].rstrip()
    for elem in citeItems:
        elem = elem.replace('<i>','*')
        elem = elem.replace('</i>','*')
        elem = elem.replace('<em>','*')
        elem = elem.replace('</em>','*')        
        output += f'{elem}'
    output += '\n\n'

ai = 0
desc_i = 0
for i in range(len(texts)):
    if not texts[i] == all_texts[ai]:      
        output += f'## {all_texts[ai]}\n\n'
        ai+=1
    if types[desc_i].find("Bookmark") != -1: 
        output += f'*Bookmark* @{pages[desc_i]}\n'
        output += '\n'    
        desc_i +=1
    if types[i].find("Note") != -1: 
        output += f'\t> {texts[i]}\n' # blockquote my notes
        output += f'\t{types[desc_i]}@{pages[desc_i]}\n'
        output += '\n'
        
    else:        
        if types[desc_i].find("yellow") != -1:
            output += f'- {texts[i]} ({authors} @{pages[desc_i]})\n\n'
        elif types[desc_i].find("pink") != -1:
            output += f'- [[Disagreement]] {texts[i]} ({authors} @{pages[desc_i]})\n\n'
        elif types[desc_i].find("blue") != -1:
            output += f'- [[Important]] {texts[i]} ({authors} @{pages[desc_i]})\n\n'
        elif types[desc_i].find("orange") != -1:
            output += f'- [[Idea]] {texts[i]} ({authors} @{pages[desc_i]})\n\n'              


        # output += f'\t{types[desc_i]}@{pages[desc_i]}\n'
        # output += '\n'
    ai+=1
    desc_i +=1

try:
    dest.write_text(output, encoding='UTF-8')
except OSError as e:
    print(f'Failed to write file: {e}')
    exit(1)
print(f'Written to: {dest_name}')
