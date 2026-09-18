import numpy as np
import cv2
from tensorflow.keras.models import load_model
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response

model = load_model("facemood_model.keras")
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

emotion_labels = {
    0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy",
    4: "Sad", 5: "Surprise", 6: "Neutral"
}

@method_decorator(ensure_csrf_cookie, name="get")
class PredictEmotionView(APIView):

    def get(self, request):
        return Response({"detail": "CSRF cookie set"})

    def post(self, request):
        image_file = request.FILES.get("image")

        if image_file is None:
            return Response({"error": "No image provided"}, status=400)

        file_bytes = np.frombuffer(image_file.read(), np.uint8)
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            return Response({"error": "No face detected"}, status=400)

        x, y, w, h = faces[0]
        face_crop = gray[y:y+h, x:x+w]
        face_resized = cv2.resize(face_crop, (48, 48))
        face_normalized = face_resized / 255.0
        face_input = face_normalized.reshape(1, 48, 48, 1)

        prediction = model.predict(face_input, verbose=0)
        emotion_index = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        return Response({
            "emotion": emotion_labels[emotion_index],
            "confidence": round(confidence, 4)
        })