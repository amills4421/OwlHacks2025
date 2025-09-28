from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
#from .models import TaskReference
import os

from .ml.clip_model import get_image_embedding, cosine_similarity
from .ml.blip2_model import generate_caption

class compare_clean(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        task_id = request.data.get("task_id")
        uploaded_image = request.data.get("image")

        # Save uploaded file temporarily
        file_path = default_storage.save(uploaded_image.name, uploaded_image)

        # Load reference image (for demo, assume it's static in ./references)
        reference_path = os.path.join("references", f"{task_id}.jpg")

        # Get embeddings
        ref_emb = get_image_embedding(reference_path)
        new_emb = get_image_embedding(file_path)

        # Compute similarity
        score = cosine_similarity(ref_emb, new_emb)
        feedback = "Looks clean!" if score > 0.9 else "Needs improvement."

        return Response({
            "task_id": task_id,
            "score": float(score),
            "feedback": feedback
        })

class analyze_image(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        uploaded_image = request.data.get("image")
        file_path = default_storage.save(uploaded_image.name, uploaded_image)

        try:
            caption = generate_caption(file_path, prompt="What looks disorganized here?")
        finally:
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

        return Response({
            "caption": caption,
            "feedback": f"AI detected: {caption}"
        })
