import torch
from transformers import BitsAndBytesConfig, Qwen2_5_VLForConditionalGeneration, AutoProcessor
from accelerate import infer_auto_device_map
from vision_process import process_vision_info  # Ensure this script is present

# Configure quantization for better memory efficiency
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    llm_int8_enable_fp32_cpu_offload=True
)

# Set device map for optimized memory allocation
device_map = {"cpu": "8GB", 0: "8GB"}  # Adjust memory allocation based on your system
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2.5-VL-3B-Instruct",
    torch_dtype=torch.float16,
    device_map=device_map,
    quantization_config=quantization_config
)

# Load processor with reduced visual token limits
min_pixels = 128 * 28 * 28
max_pixels = 640 * 28 * 28
processor = AutoProcessor.from_pretrained(
    "Qwen/Qwen2.5-VL-3B-Instruct",
    min_pixels=min_pixels,
    max_pixels=max_pixels
)

# Define the input image and text prompt
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "demo.jpeg"},
            {"type": "text", "text": "Describe this image."},
        ],
    }
]

# Process inputs
text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text], images=image_inputs, videos=video_inputs, padding=True, return_tensors="pt"
).to(model.device)

# Generate response
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)

# Display output
print(output_text)
