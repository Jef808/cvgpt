#!/usr/bin/env python3

import sys
from pathlib import Path
from common import do_prompt, get_job_description_and_company_name

def make_payload(company_name, job_description):
  return  {
    "model" : "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": (
            f"Perform a focused internet search on {company_name} to obtain key information relevant to provided job offer listing."
            "Concentrate on extracting concise, pertinent details that will directly assist in tailoring a resume for the specific job offer."
        )
      },
      {
        "role": "user",
        "content": f"I have a job offer listing from {company_name}. Here it is:\n {job_description}. I need you to quickly find and summarize the most important information about OpenAsset that I should include in my resume for this job."
      }
    ]
  }

def main(filepath: Path):
    company_name, job_description = get_job_description_and_company_name(filepath)

    payload = make_payload(company_name, job_description)
    response = do_prompt(payload)
    print(response)


if __name__ == '__main__':
  filepath = Path(sys.argv[1])
  main(filepath)
