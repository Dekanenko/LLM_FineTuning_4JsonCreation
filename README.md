# Llama 1B for JSON

A project for fine-tuning Llama 1B models to generate structured JSON outputs.

## Overview

This project focuses on fine-tuning small Llama models (1B parameters) to improve their ability to generate valid, well-structured JSON responses. The fine-tuning process uses synthetic data generated with larger language models to teach the smaller model how to properly format and structure JSON outputs for various use cases.

## Project Structure

- `src/` - Core source code
  - `models.py` - Pydantic models defining the JSON schemas
  - `prompts.py` - Prompt templates for synthetic data generation
  - `synthetic_generation.py` - Code for generating synthetic training data
  - `utils.py` - Utility functions for data processing
  - `langchain_llm_wrapper.py` - LangChain wrapper for the fine-tuned model
- `data/` - Training and evaluation datasets
- `notebooks/` - Jupyter notebooks for training and evaluation

## Fine-tuning Process

The fine-tuning process consists of several key steps:

1. **Synthetic Data Generation**: Using GPT-4o-mini to generate high-quality JSON examples based on predefined schemas
   - The `create_dataset.ipynb` notebook demonstrates this process
   - Each example consists of an input prompt and a corresponding JSON output

2. **Data Preparation**: Converting the synthetic data into a format suitable for fine-tuning
   - The data is tokenized and formatted with appropriate instruction templates

3. **Model Fine-tuning**: Training a Llama 1B model on the prepared dataset
   - Using Parameter-Efficient Fine-Tuning (PEFT) techniques like LoRA
   - Optimizing for JSON structure and validity

4. **Evaluation**: Testing the fine-tuned model on new prompts to ensure it generates valid JSON

## Getting Started

### Prerequisites

- Python 3.8+
- CUDA-compatible GPU (recommended for training)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Llama1B-for-JSON.git
cd Llama1B-for-JSON
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

### Running the Project

1. Generate synthetic data:
```bash
jupyter notebook create_dataset.ipynb
```

2. Fine-tune the model:
```bash
jupyter notebook finetune_model.ipynb
```

3. Evaluate the fine-tuned model:
```bash
jupyter notebook evaluate_model.ipynb
```

## Use Cases

The fine-tuned model can be used for various applications requiring structured JSON output:
- Extracting structured information from text
- Converting natural language to API requests
- Generating structured data for applications
- Creating consistent data formats for downstream processing

## License

[MIT License](LICENSE) 