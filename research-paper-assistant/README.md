# Automated Research Paper Summarizer and Title Generator

This project aims to assist researchers by automating the process of summarizing scientific papers and generating appropriate titles.

## Features

- **Text Summarization**: Implements extractive and abstractive summarization techniques to condense research papers into concise summaries.
- **Title Generation**: Utilizes a fine-tuned GPT-2 model to generate relevant and catchy titles for research papers.
- **Keyword Extraction**: Implements TF-IDF and other NLP techniques to extract main keywords from the papers.
- **Domain Classification**: Develops a classifier to categorize papers into different scientific domains for better organization and searchability.

## Installation

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```sh
python src/main.py
```

## Directory Structure

```
research-paper-assistant
├── src
│   ├── main.py
│   ├── summarizer
│   ├── title_generator
│   ├── keyword_extraction
│   ├── domain_classifier
│   └── utils
├── tests
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## Author

This project was developed by DevSAllen.

## License

This project is licensed under the MIT License.