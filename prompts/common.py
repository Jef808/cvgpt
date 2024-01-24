from openai import OpenAI
import subprocess
import os


class API:
    def notify(message):
        subprocess.run(["notify-send", message])

    def get_api_key(cls):
        return os.getenv("OPENAI_API_KEY")

    def __init__(self, *, default_model="gpt-3.5-turbo"):
        self.total_tokens = 0
        self.client = OpenAI(api_key=API.get_api_key())
        self.default_model = default_model

    def __call__(self, *, payload, output=None, model=None):
        API.notify("Prompting OpenAI...")

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
