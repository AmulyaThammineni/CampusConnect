from django.urls import path
from .views import chatbot_page, chatbot_response, upload_file

urlpatterns = [
    path("", chatbot_page, name="chatbot_page"),
    path("ask/", chatbot_response, name="chatbot_response"),
    path("upload/", upload_file, name="upload_file"),
]
