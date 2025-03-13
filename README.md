Here's a comprehensive README.md file for the PPT Translator project:

```markdown
# PPT Translator

A Python-based tool for translating PowerPoint presentations using the DeepL API.

## Prerequisites

- Python 3.8 or higher
- DeepL API key
- Git (for cloning the repository)

## Setup Instructions

### Ubuntu

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ppt-translator.git
cd ppt-translator
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file:
```bash
echo "DEEPL_API_KEY=your-api-key-here" > .env
```

### Windows

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ppt-translator.git
cd ppt-translator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file:
```bash
echo DEEPL_API_KEY=your-api-key-here > .env
```

## Project Structure

```
ppt-translator/
├── inputs/          # Place input PPTX files here
├── outputs/         # Translated files will be saved here
├── main.py         # Main translation script
├── requirements.txt # Project dependencies
└── .env            # Environment variables
```

## Usage

### Interactive Mode

1. Place your PPTX files in the `inputs` directory
2. Run the script:
```bash
python main.py
```
3. Follow the interactive prompts to:
   - Select source language
   - Select target language
   - Choose input file

### Command Line Mode

Use command line arguments for batch processing:

```bash
python main.py --source SOURCE_LANG --target TARGET_LANG --input INPUT_FILE --output OUTPUT_FILE
```

Example:
```bash
python main.py --source en --target fr --input ./inputs/presentation.pptx --output ./outputs/presentation_fr.pptx
```

## Supported Languages

- Czech (cs)
- German (de)
- English (en)
- Spanish (es)
- Estonian (et)
- Finnish (fi)
- French (fr)
- Indonesian (id)
- Italian (it)
- Japanese (ja)
- Norwegian (nb-NO)
- Portuguese (pt)
- Russian (ru)
- Vietnamese (vi)
- Chinese Simplified (zh-Hans)


## Notes

- Ensure you have a valid DeepL API key
- Large presentations may take longer to translate
- Some text patterns (like language codes) are automatically handled
- Translated files are saved in the `outputs` directory

