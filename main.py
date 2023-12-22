import os
import logging
import argparse
import datetime
from typing import Optional
from dotenv import load_dotenv
from google.generativeai import GenerativeModel, configure
from markdownify import markdownify
import signal
import sys

class Config:
    def __init__(self):
        load_dotenv()
        self.api_key = self.get_env_var('API_KEY')
        self.model_name = self.get_env_var('MODEL_NAME', default='gemini-pro')
        self.log_level = self.get_env_var('LOG_LEVEL', default='INFO')

    @staticmethod
    def get_env_var(name: str, default: Optional[str] = None) -> str:
        value = os.getenv(name, default)
        if value is None:
            raise ValueError(f"The environment variable '{name}' is not set.")
        return value

def setup_logging(level: str, log_file: str = 'app.log'):
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {level}')
    logging.basicConfig(level=numeric_level,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(log_file),
                            logging.StreamHandler()
                        ])

def generate_content(api_key: str, model_name: str) -> None:
    configure(api_key=api_key)
    model = GenerativeModel(model_name=model_name)
    prompt = input("Please enter your prompt: ").strip()
    response = model.generate_content(prompt)
    logging.info(response.text)

def chat_session(api_key: str, model_name: str, output_file: str) -> None:
    configure(api_key=api_key)
    model = GenerativeModel(model_name=model_name)
    session_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    with open(output_file, 'a') as file:
        while True:
            prompt = input("Please enter your prompt: ").strip()
            if prompt.lower() == 'exit':
                break
            response = model.generate_content(prompt)
            markdown_text = markdownify(response.text)
            print(markdown_text)
            file.write(f"Session {session_id}: {markdown_text}\n\n")

def signal_handler(sig, frame):
    print('You pressed Ctrl+C! Exiting gracefully.')
    sys.exit(0)

def main() -> None:
    parser = argparse.ArgumentParser(description='Content and Chat Generator')
    parser.add_argument('--output', help='Output file for chat responses', default='RESPONSE.md')
    parser.add_argument('--loglevel', help='Set the logging level (e.g., INFO, DEBUG)', default='INFO')
    parser.add_argument('--logfile', help='Log file name', default='app.log')
    args = parser.parse_args()

    config = Config()
    setup_logging(args.loglevel or config.log_level, args.logfile)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        while True:
            choice = input("Choose mode - Content (C) or Chat (Ch): ").strip().lower()
            if choice not in ['c', 'ch']:
                print("Invalid choice. Please enter 'C' for Content or 'Ch' for Chat.")
                continue

            if choice == 'c':
                generate_content(config.api_key, config.model_name)
            else:
                chat_session(config.api_key, config.model_name, args.output)
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
