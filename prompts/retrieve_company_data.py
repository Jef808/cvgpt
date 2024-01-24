#!/usr/bin/env python3

import sys
from openai import OpenAI
from pathlib import Path
from common import notify, get_api_key

def make_payload(company_name, job_offer_listing):
  return  {
    "model": "gpt-3.5-turbo",
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

def get_job_description_and_company_name(filepath):
    job_description = open(filepath, "r").read()
    company_name = filepath.stem
    return company_name, job_description


def main(filepath: Path):
    notify("starting script: " + __file__)
    company_name, job_description = get_job_description_and_company_name(filepath)

    payload = make_payload(company_name, job_description)

    notify("prompting")
    openai_client = OpenAI(api_key=get_api_key())
    response = openai_client.chat.completions.create(**payload)

    notify("got response")
    py_response = response.model_dump()
    content = py_response['choices'][0]['message']['content']

    print(content)


if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    main(filepath)
