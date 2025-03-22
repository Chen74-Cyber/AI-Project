# Qwen 2.5 VL - Vision-Language Model  

## 📌 Overview  

Qwen 2.5 VL is an advanced **vision-language model** capable of understanding images and generating meaningful textual descriptions. This repository provides a setup guide for **running Qwen 2.5 VL** on a local machine using **Python**.  

---

## 🛠️ Installation  

### 1️⃣ Clone or Download the Repository  

#### Option 1: Clone  

```sh
git clone https://github.com/QwenLM/Qwen2.5-VL.git
cd Qwen2.5-VL
```

#### Option 2: Download ZIP  

1. Visit [Qwen2.5-VL GitHub](https://github.com/QwenLM/Qwen2.5-VL)  
2. Click "**Code**" → "**Download ZIP**"  
3. Extract and navigate to the folder  

### 2️⃣ Install Dependencies  

Ensure you have **Python 3.8+** installed. Then, install the required packages:  

```sh
pip install torch transformers accelerate bitsandbytes
```

For **CUDA-enabled GPUs**, install PyTorch with CUDA:  

```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
