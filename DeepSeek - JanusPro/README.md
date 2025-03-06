# DeepSeek - JanusPro Installation Guide
## Introduction
DeepSeek JanusPro is a cutting-edge AI model designed for advanced natural language processing and image-related tasks. Built by DeepSeek AI, JanusPro harnesses the power of deep learning to deliver state-of-the-art text generation, understanding, and image detection capabilities. Whether you're developing AI-powered applications, enhancing automation, or exploring creative AI solutions, JanusPro provides a robust and scalable foundation. With easy integration via Hugging Face and a user-friendly web interface, it empowers researchers, developers, and businesses to push the boundaries of artificial intelligence. 🚀


## Clone the Repository
Clone the official Janus repository:
```bash
git clone https://lnkd.in/eHu7bVr5
```

## Set Up Python Environment
Ensure Python is installed. Then, create and activate a virtual environment:

### For Linux/Mac:
```bash
python -m venv <your_venv_name>
source <your_venv_name>/bin/activate
```

### For Windows:
```bash
python -m venv <your_venv_name>
<your_venv_name>\Scripts\activate
```

## Install Hugging Face Hub
Install the Hugging Face package using pip:
```bash
pip install huggingface_hub
```

## Download the Model
Run the following Python code to download the JanusPro model:
```python
from huggingface_hub import snapshot_download
snapshot_download(repo_id="deepseek-ai/Janus-Pro-7B", local_dir="/path/to/your/Janus")
```

## Install Necessary Libraries
After downloading the model, navigate to the directory and install the required libraries:
```bash
pip install -e .
```

## Image Detection & Generation Models
You can find the models for image detection and image generation here:
[DeepSeek Image Models](https://lnkd.in/eKHkAt9E)


## Web UI Installation
To run the web UI, install Gradio:
```bash
pip install gradio
```

From the demo directory, run:
```bash
python app_januspro.py
```

You’ll get a local host URL to access the demo and interact with JanusPro via your browser.

