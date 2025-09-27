import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def get_image_embedding(image_path):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    with torch.no_grad():
        embedding = model.encode_image(image)
    return embedding.cpu()

def cosine_similarity(vec1, vec2):
    v1 = vec1 / vec1.norm(dim=-1, keepdim=True)
    v2 = vec2 / vec2.norm(dim=-1, keepdim=True)
    return torch.matmul(v1, v2.T).item()
