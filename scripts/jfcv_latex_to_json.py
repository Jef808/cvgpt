#!/usr/bin/env python3
import re
import json
import sys

def extract_sections(latex_content, section_titles):
    sections = {}
    for title in section_titles:
        pattern = rf"\\cvsection\{{({title})\}}(.*?)\\cvsection"  # Pattern to find each section
        matches = re.findall(pattern, latex_content, re.DOTALL | re.IGNORECASE)
        if matches:
            sections[title] = matches[0][1]  # Extract the content of each section
    return sections

def extract_info_from_section(section_content):
    items = []
    pattern = r"\\cvevent\{(.*?)\}\{(.*?)\}\{(.*?)\}\{(.*?)\}(.*?)\\divider"
    matches = re.findall(pattern, section_content, re.DOTALL | re.IGNORECASE)
    for match in matches:
        item = {
            "position": match[0].strip(),
            "organization": match[1].strip(),
            "date": match[2].strip(),
            "location": match[3].strip(),
            "details": match[4].strip()
        }
        items.append(item)
    return items

def latex_to_json(latex_content):
    sections_to_extract = ["Work Experience", "Education"]
    extracted_sections = extract_sections(latex_content, sections_to_extract)
    json_data = {}
    for section_title in sections_to_extract:
        if section_title in extracted_sections:
            section_data = extract_info_from_section(extracted_sections[section_title])
            json_key = section_title.lower().replace(" ", "_")
            json_data[json_key] = section_data
    return json.dumps(json_data, indent=4)

def clean_latex_text(text):
    # Remove LaTeX commands
    clean_text = re.sub(r"\\[a-zA-Z]+\{", "", text)
    clean_text = re.sub(r"\}", "", clean_text)
    clean_text = re.sub(r"\\hspace\{.*?\}", "", clean_text)  # Remove \hspace commands
    clean_text = re.sub(r"\\emph\{", "", clean_text)  # Remove \emph commands
    clean_text = re.sub(r"\\textbf\{", "", clean_text)  # Remove \textbf commands
    clean_text = re.sub(r"\\item", "", clean_text)  # Remove \item commands
    clean_text = re.sub(r"\\begin\{itemize\}", "", clean_text)  # Remove \begin{itemize}
    clean_text = re.sub(r"\\end\{itemize\}", "", clean_text)  # Remove \end{itemize}
    clean_text = re.sub(r"itemize", "", clean_text)
    clean_text = re.sub(r"\n", " ", clean_text)
    clean_text = clean_text.strip()

    # Replace unicode escape sequences
    unicode_replacements = {
        r"\u00e9": "é", r"\u00e8": "è", r"\u00ea": "ê", r"\u00eb": "ë",
        r"\u00e0": "à", r"\u00e2": "â", r"\u00ee": "î", r"\u00ef": "ï",
        r"\u00f4": "ô", r"\u00fb": "û", r"\u00fc": "ü", r"\u00c9": "É",
        r"\u00c8": "È", r"\u00ca": "Ê", r"\u00cb": "Ë", r"\u00c0": "À",
        r"\u00c2": "Â", r"\u00ce": "Î", r"\u00cf": "Ï", r"\u00d4": "Ô",
        r"\u00db": "Û", r"\u00dc": "Ü", r"\u00e7": "ç", r"\u00c7": "Ç"
    }

    for unicode_code, char in unicode_replacements.items():
        clean_text = clean_text.replace(unicode_code, char)

    return clean_text

def process_json(json_data):
    for key in json_data:
        for entry in json_data[key]:
            entry['position'] = clean_latex_text(entry['position'])
            entry['organization'] = clean_latex_text(entry['organization'])
            entry['date'] = clean_latex_text(entry['date'])
            entry['location'] = clean_latex_text(entry['location'])
            entry['details'] = clean_latex_text(entry['details'])
    return json_data


with open(sys.argv[1], 'r') as f:
    latex_content = f.read()

result = latex_to_json(latex_content)
json_data = json.loads(result)
cleaned_json = process_json(json_data)
print(json.dumps(cleaned_json, indent=4, ensure_ascii=False))
