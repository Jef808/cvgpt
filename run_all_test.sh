#!/bin/bash

echo convert resume to json
python scripts/jfcv_latex_to_json.py data/cv/jfcv.tex > data/cvjson/jf.cvjson.txt

echo retrieve company data
python prompts/retrieve_company_data.py data/job_descriptions/OpenAsset.txt > data/company_info/OpenAsset.companyinfo.txt

echo summarize job description
python prompts/summarize_job_description.py data/job_descriptions/OpenAsset.txt > data/job_description_summaries/OpenAsset.jobdescriptionsummary.txt
