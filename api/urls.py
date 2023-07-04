from django.urls import path,include
from .views import BookList, BookDetail

app_name = "api"

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('books',BookList.as_view(),name="books"),
    path('book/<str:pk>/',BookDetail.as_view(),name="bookdetails"),    
]