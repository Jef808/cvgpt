#!/usr/bin/env python3

import os
import sys
import subprocess
from openai import OpenAI
from pathlib import Path

DEFAULT_MODEL = "gpt-4"

def make_payload(*, company_name, job_description):
  return  {
    "model" : "gpt-4",
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


def get_api_key():
    return os.getenv('OPENAI_API_KEY')

def notify(message):
  subprocess.run(["notify-send", message])

def main():
    notify("starting script: " + __file__)
    openai_client = OpenAI(api_key=get_api_key())

    filepath = Path(sys.argv[1])
    job_description = open(filepath, "r").read()
    company_name = filepath.name

    payload = make_payload(company_name=company_name, job_description=job_description)

    notify("prompting")
    response = openai_client.chat.completions.create(**payload)
    py_response = response.model_dump()

    content = py_response['choices'][0]['message']['content']

    print(content)


if __name__ == '__main__':
    main()
