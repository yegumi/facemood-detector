from django.urls import path
from .views import PredictEmotionView

urlpatterns = [
    path("predict/", PredictEmotionView.as_view(), name="predict_emotion"),
]