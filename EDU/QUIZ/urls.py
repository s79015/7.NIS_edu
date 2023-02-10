from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "quiz"   

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:quiz_id>/", views.display_quiz, name="display_quiz"),
    path("<int:quiz_id>/questions/<int:question_id>", views.display_question, name="display_question"),
    path("questions/<int:question_id>/grade/", views.grade_question, name="grade_question"),
    # path("", views.nav_hor, name="base" ),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)