#!/usr/bin/env python3

import sys
from pathlib import Path
from common import notify, get_api_key, do_prompt,get_job_description_and_company_name

def make_payload(company_name, job_offer_listing):
  return  {
    "model": "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": f"Perform a focused internet search on {company_name} to obtain key information relevant to the {job_offer_listing}. Concentrate on extracting concise, pertinent details that will directly assist in tailoring a resume for the specific job offer."
      },
      {
        "role": "user",
        "content": f"I have a job offer listing from {company_name}. Here it is: {job_offer_listing}. I need you to quickly find and summarize the most important information about {company_name} that I should include in my resume for this job. "
                    "For each information chunk, show me the url of where you retrieved it."
      }
    ],
  }

def main(filepath: Path):
    notify("starting script: " + __file__)
    company_name, job_description = get_job_description_and_company_name(filepath)

    payload = make_payload(company_name, job_description)
    response = do_prompt(payload)
    print(response)

if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    main(filepath)
