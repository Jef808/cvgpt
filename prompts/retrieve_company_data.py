#!/usr/bin/env python3
#!/usr/bin/env python3

import sys
from openai import OpenAI
from pathlib import Path
from common import notify, get_api_key

def make_payload(company_name, job_offer_listing):
  return  {
    "model": "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": f"Use internet search tools to explore and collect creative and engaging information about {company_name} that resonates with the essence of the {job_offer_listing}. Focus on unique aspects like company initiatives, culture, and employee experiences that will inspire a distinctive and compelling customization of a resume for this job opportunity."
      },
      {
        "role": "user",
        "content": f"Here's a job offer I'm excited about from {company_name}: {job_offer_listing}. I want to create a resume that really stands out. Please find interesting and unique information about {company_name} that I can use to make my resume creative and engaging."
                   "For each information chunk, show me the url of where you retrieved it."
      }
    ]
  }

def get_job_description_and_company_name(filepath):

    job_description = open(filepath, "r").read()
    company_name = filepath.name
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
