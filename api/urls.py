from django.urls import path, include
from tastypie.api import Api
from .models import PostResource

api = Api(api_name='v1')
api.register(PostResource())

urlpatterns = [
  path('', include(api.urls), name='api'),
]