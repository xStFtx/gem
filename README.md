## Gem: Gemini AI Tester 🎒✨

Dive into the realm of automated storytelling with "Gem", a tool that harnesses the power of Google's Generative AI to conjure narratives centered around a mystical backpack. "Gem" is crafted for storytellers, writers, and anyone yearning to explore the bounds of their imagination.

## Getting Started

Embark on your journey with Gem by obtaining an API key from Google's MakerSuite. Follow the instructions below to prepare your environment and start weaving tales with the aid of AI.

### Prerequisites

- Python 3.6 or newer
- Internet connection for API communication

### Installation

``
git clone https://github.com/xStFtx/gem.git
cd gem
``

### API Key Configuration

``
cp .env_example .env
nano .env  # Feel free to use your preferred text editor
``

Populate the `.env` file with your API key like so:

``
API_KEY=your_actual_api_key_here
``

Ensure `your_actual_api_key_here` is replaced with the actual API key you got from Google MakerSuite.

### Usage

Run Gem to generate your story using the following command:

``
python3 main.py
``

Let the magic unfold as Gem narrates a unique story about the magic backpack.

## Features

- **Automated Story Generation**: Create enchanting stories with a mere command.
- **Streamlined Configuration**: Utilize a `.env` file for straightforward API key management.
- **Flexibility**: Tailor the narrative prompt to spawn various story genres.


For comprehensive guidance on Gem's functionalities and customization options, visit our [documentation page](https://github.com/your-username/gem/wiki).

## Contributing

Your contributions can help make Gem an even more splendid tool for AI-powered storytelling. We welcome all contributions with open arms!

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgements

- Google's MakerSuite for the AI magic
- The wonderful community of contributors and supporters
