from django.urls import path
from .views import redirect_view, urlshortner

urlpatterns = [
    path('url_tfugifier/', urlshortner, name='urlshortner'),
    path('<str:code>/', redirect_view, name='redirect_view'),
    
]
