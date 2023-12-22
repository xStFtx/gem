import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

def get_api_key(env_variable_name: str) -> str:
    api_key = os.getenv(env_variable_name)
    if not api_key:
        raise ValueError(f"The environment variable '{env_variable_name}' is not set.")
    return api_key

def generate_content(api_key: str, prompt: str) -> None:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name='gemini-pro')
        response = model.generate_content(prompt)
        logging.info(response.text)
    except Exception as e:
        logging.error(f"Error generating content: {e}")

def handle_chat(api_key: str, prompt: str) -> None:
    try:
        chat = genai.start_chat()
        response = chat.send_message(prompt)
        logging.info(response.text)
    except Exception as e:
        logging.error(f"Error in chat: {e}")

def main() -> None:
    try:
        api_key = get_api_key('API_KEY')

        while True:
            choice = input("Choose mode - Content (C) or Chat (Ch): ").strip().lower()
            if choice in ['c', 'ch']:
                break
            print("Invalid choice. Please enter 'C' for Content or 'Ch' for Chat.")

        user_prompt = input("Please enter your prompt: ").strip()

        if choice == 'c':
            generate_content(api_key, user_prompt)
        else:
            handle_chat(api_key, user_prompt)
    except Exception as e:
        logging.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
