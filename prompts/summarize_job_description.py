#!/usr/bin/env python3

import sys
from openai import OpenAI
from pathlib import Path
from common import notify, get_api_key

def make_payload(company_name, job_description):
  return  {
    "model" : "gpt-4-1106-preview",
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

def get_job_description_and_company_name(filepath):
    job_description = open(filepath, "r").read()
    company_name = filepath.name
    return company_name, job_description

def main():
    notify("starting script: " + __file__)
    filepath = Path(sys.argv[1])
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
    main()