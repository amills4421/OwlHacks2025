from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import TaskReference
from .ml.clip_model import get_image_embedding, cosine_similarity

class CompareClean(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        task_id = request.data.get("task_id")
        image_file = request.data.get("image")

        # Get user reference image from DB
        reference = TaskReference.objects.get(task_id=task_id, user=request.user)

        # Compute embeddings
        ref_embedding = get_image_embedding(reference.image.path)
        new_embedding = get_image_embedding(image_file)

        score = cosine_similarity(ref_embedding, new_embedding)

        feedback = "Looks clean!" if score > 0.8 else "Needs improvement."

        return Response({
            "task_id": task_id,
            "score": float(score),
            "feedback": feedback
        })
