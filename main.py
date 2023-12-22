import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai
import markdownify

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

def get_api_key(env_variable_name: str) -> str:
    api_key = os.getenv(env_variable_name)
    if not api_key:
        raise ValueError(f"The environment variable '{env_variable_name}' is not set.")
    return api_key

# Global API configuration
api_key = get_api_key('API_KEY')
genai.configure(api_key=api_key)

def generate_content(prompt: str) -> None:
    try:
        model = genai.GenerativeModel(model_name='gemini-pro')
        response = model.generate_content(prompt)
        logging.info(response.text)
    except Exception as e:
        logging.error(f"Error generating content: {e}")



def chat() -> None:
    try:
        model = genai.GenerativeModel('gemini-pro')
        with open('RESPONSE.md', 'w') as file:  # Open the file in write mode
            while True:
                prompt = input("Please enter your prompt: ").strip()
                response = model.generate_content(prompt)
                markdown_text = markdownify.markdownify(response.text)
                print(markdown_text)
                file.write(markdown_text + '\n\n')  # Write to the file and add a newline for separation
    except Exception as e:
        logging.error(f"Error in chat: {e}")


def main() -> None:
    try:
        while True:
            choice = input("Choose mode - Content (C) or Chat (Ch): ").strip().lower()
            if choice in ['c', 'ch']:
                break
            print("Invalid choice. Please enter 'C' for Content or 'Ch' for Chat.")

        user_prompt = input("Please enter your prompt: ").strip()

        if choice == 'c':
            generate_content(user_prompt)
        else:
            chat()
    except Exception as e:
        logging.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
