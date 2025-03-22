# DeepSeek - JanusPro 
## Introduction
DeepSeek JanusPro is a cutting-edge AI model designed for advanced natural language processing and image-related tasks. Built by DeepSeek AI, JanusPro harnesses the power of deep learning to deliver state-of-the-art text generation, understanding, and image detection capabilities. Whether you're developing AI-powered applications, enhancing automation, or exploring creative AI solutions, JanusPro provides a robust and scalable foundation. With easy integration via Hugging Face and a user-friendly web interface, it empowers researchers, developers, and businesses to push the boundaries of artificial intelligence. 🚀

# 📋 System Requirements for DeepSeek JanusPro

**OS:** Windows (WSL recommended), macOS (limited), Linux (Ubuntu 20.04+)<br>
**Storage:** 50GB+ free space (SSD/NVMe recommended)<br>
**RAM:** 8GB (minimum), 16GB+ (recommended), 32GB+ (for full precision)<br>
**CPU:** Multi-core (Intel i5 10th Gen / AMD Ryzen 5 or better)<br>
**GPU:** RTX 3060 (12GB VRAM) minimum, RTX 4090 / A100 (24GB+ VRAM) recommended<br>
**Libraries:** `torch`, `transformers`, `huggingface_hub`, `opencv-python`, `gradio`, `numpy`, `safetensors`, `diffusers`



# Installation Guide
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

---

## 🔗 References
- **DeepSeek AI JanusPro on Hugging Face**: [https://huggingface.co/deepseek-ai/Janus-Pro-7B](https://huggingface.co/deepseek-ai/Janus-Pro-7B)
- **DeepSeek AI Janus GitHub Repository**: [https://github.com/deepseek-ai/Janus](https://github.com/deepseek-ai/Janus)

