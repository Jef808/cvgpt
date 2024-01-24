import subprocess
import os


def get_api_key():
    return os.getenv('OPENAI_API_KEY')

def notify(message):
  subprocess.run(["notify-send", message])