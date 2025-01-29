import argparse
import json
import logging
from pathlib import Path
from typing import Optional
from datetime import datetime

from summarizer.extractive import ExtractiveSummarizer
from summarizer.abstractive import AbstractiveSummarizer
from title_generator.gpt2_model import TitleGenerator
from keyword_extraction.tfidf import KeywordExtractor
from domain_classifier.classifier import DomainClassifier

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PaperProcessor:
    """Paper Processing Utility Class"""
    SAMPLE_PAPER_CONTENT = """Title: Deep Learning Applications in Natural Language Processing

Abstract:
This paper explores recent advances in deep learning applications for natural language processing tasks.

Introduction:
Natural Language Processing (NLP) has seen significant advancement with deep learning models.

Methods:
We employed transformer-based architectures and modern NLP techniques.

Results:
Our experiments show significant improvements over baseline methods.

Conclusion:
The results demonstrate the effectiveness of deep learning in NLP tasks.
"""

    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.data_dir = self.base_dir / "data"
        self.input_dir = self.data_dir / "input"
        self.output_dir = self.data_dir / "output"
        self.setup_directories()

    def setup_directories(self) -> None:
        """Create necessary directory structure"""
        dirs = [self.data_dir, self.input_dir, self.output_dir]
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)

    def create_sample_paper(self) -> Path:
        """Create a sample paper if none exists"""
        sample_path = self.input_dir / "sample_paper.txt"
        sample_path.write_text(self.SAMPLE_PAPER_CONTENT, encoding='utf-8')
        return sample_path

def setup_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Research Paper Analyzer')
    parser.add_argument(
        '--input',
        type=str,
        default='data/input/sample_paper.txt',
        help='Path to the input paper file'
    )
    return parser

def read_paper(file_path: Path) -> Optional[str]:
    """Read and return the contents of a paper file."""
    try:
        return file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        return None

def process_paper(text: str) -> dict:
    """Process the paper and return results."""
    try:
        # Initialize components with text
        extractive_summarizer = ExtractiveSummarizer(text)
        abstractive_summarizer = AbstractiveSummarizer(text)
        title_generator = TitleGenerator(text)
        keyword_extractor = KeywordExtractor(text)
        domain_classifier = DomainClassifier(text)

        return {
            'extractive_summary': extractive_summarizer.generate_summary(),
            'abstractive_summary': abstractive_summarizer.generate_summary(),
            'generated_title': title_generator.generate_title(),
            'keywords': keyword_extractor.extract_keywords(),
            'domain': domain_classifier.classify()
        }
    except Exception as e:
        logger.error(f"Error processing paper: {e}")
        return {}

def main():
    # Initialize paper processor
    processor = PaperProcessor()

    # Parse arguments
    parser = setup_argparse()
    args = parser.parse_args()

    # Handle input path
    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = processor.input_dir / input_path.name

    # Create sample paper if needed
    if not input_path.exists():
        logger.info("Creating sample paper...")
        input_path = processor.create_sample_paper()
        logger.info(f"Created sample paper at {input_path}")

    # Process paper
    text = read_paper(input_path)
    if text:
        results = process_paper(text)
        if results:
            # Save results to output directory
            output_file = processor.output_dir / f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=4)
            logger.info(f"Results saved to {output_file}")

            # Display results
            print("\nAnalysis Results:")
            for key, value in results.items():
                print(f"\n{key.replace('_', ' ').title()}:")
                print(f"{value}")
        else:
            logger.error("Failed to process paper")

if __name__ == "__main__":
    main()