from django.urls import path
from .views import (
  index, about, contacts, tags, 
  categories, post, change_language,
  category
)

urlpatterns = [
  path('', index, name='index'),
  path('about/', about, name='about'),
  path('contacts/', contacts, name='contacts'),
  path('tags/<slug:tag_slug>/', tags, name='tags'),
  path('categories/', categories, name='categories'),
  path('category/<slug:cat_slug>/', category, name='category'),
  path('<slug:cat_slug>/<slug:post_slug>/', post, name='post'),
  path('set-language/', change_language, name='change_language'),
]