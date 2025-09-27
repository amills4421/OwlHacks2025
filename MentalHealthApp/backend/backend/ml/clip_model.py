import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def get_image_embedding(image_path):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    with torch.no_grad():
        embedding = model.encode_image(image)
    return embedding.cpu().numpy()

def cosine_similarity(vec1, vec2):
    return float((vec1 @ vec2.T) / (torch.norm(torch.tensor(vec1)) * torch.norm(torch.tensor(vec2))))
