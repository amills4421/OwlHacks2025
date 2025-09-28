import torch 
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b"

    "Salesforce/blip2-opt-2.7b",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
    ).to(device)

def generate_caption(image_path, prompts="Describe this scene."):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, text=prompts, return_tensors="pt").to(device, torch.float16 if device == "cuda" else torch.float32)

    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=100)
        
    return processor.decode(output[0], skip_special_tokens=True)
