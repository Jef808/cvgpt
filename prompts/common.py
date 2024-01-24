import subprocess
from openai import OpenAI
import json
import os

def get_api_key():
    return os.getenv('OPENAI_API_KEY')

def notify(message):
  subprocess.run(["notify-send", message])

def do_prompt(payload):
    notify("prompting")
    openai_client = OpenAI(api_key=get_api_key())
    response = openai_client.chat.completions.create(**payload)

    notify("got response")

    py_response = response.model_dump()
    content = py_response['choices'][0]['message']['content']

    usage = py_response['usage']
    print(json.dumps(usage))

    return content

def get_job_description_and_company_name(filepath):
    job_description = open(filepath, "r").read()
    company_name = filepath.name
    return company_name, job_description