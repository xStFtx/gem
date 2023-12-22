import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Function to get API key with validation
def get_api_key(env_variable_name: str) -> str:
    api_key = os.getenv(env_variable_name)
    if not api_key:
        raise ValueError(f"The environment variable '{env_variable_name}' is not set.")
    return api_key

# Function to generate content
def generate_content(api_key: str, prompt: str) -> None:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name='gemini-pro')
        response = model.generate_content(prompt)
        logging.info(response.text)
    except Exception as e:
        logging.error(f"Error generating content: {e}")

# Function to start and handle chat
def handle_chat(api_key: str) -> None:
    try:
        chat = genai.start_chat()
        response = chat.send_message('Hi, I have some questions for you.')
        logging.info(response.text)
        response = chat.send_message('What is the weather today?')
        logging.info(response.text)
    except Exception as e:
        logging.error(f"Error in chat: {e}")

# Main function to run the script
def main() -> None:
    try:
        api_key = get_api_key('API_KEY')
        generate_content(api_key, 'Tell me a story about a magic backpack.')
        handle_chat(api_key)
    except Exception as e:
        logging.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
