from openai import OpenAI
import subprocess
import json
import os

def notify(message):
        subprocess.run(["notify-send", message])

def get_api_key():
        return os.getenv('OPENAI_API_KEY')

class API:

    def __init__(self, *, default_model="gpt-3.5-turbo"):
        self.total_tokens = 0
        self.client = OpenAI(api_key=get_api_key())
        self.default_model = default_model

    def __call__(self, *, payload, output=None, model=None):
        notify("Prompting OpenAI...")

        response = self.client.chats.completions.create(
            model=model if model is not None else self.default_model,
            **payload
        )
        py_response = response.model_dump()
        self.total_tokens += py_response['usage']['total_tokens']
        content = py_response['choices'][0]['message']['content']

        if output is not None:
            with open(output, 'w+') as f:
                f.write(content)

        return content


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
