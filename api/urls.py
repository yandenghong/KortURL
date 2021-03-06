"""
*  Author:   Vincent Yim
*  FileName: urls.py
*  Software: PyCharm
*  Blog:     https://yandenghong.github.io
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from api import views

app_name = "api"
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('short_urls/', views.ShortUrlsView.as_view(), name='short_urls')
]
