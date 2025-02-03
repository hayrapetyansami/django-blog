from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.translation import activate, get_language
from django.utils import translation
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Category, Tag, Post


def index(request):
  posts = Post.objects.all().order_by('-created_at')[:10]
  data = {
    'posts': posts,
    'lang': get_language()
  }
  return render(request, 'index.html', data)

def about(request):
  return render(request, 'about.html')

def contacts(request):
  return render(request, 'contacts.html')

def tags(request, tag_slug):
  tag = get_object_or_404(Tag, tag_slug=tag_slug)
  return render(request, 'tags.html', {'tag': tag})

def category(request, cat_slug):
  cat = get_object_or_404(Category, cat_slug=cat_slug)
  posts = Post.objects.filter(category=cat)
  return render(request, 'category.html', {'cat': cat, 'posts': posts})

def categories(request):
  cats = Category.objects.all()
  return render(request, 'categories.html', {'cats': cats})

def post(request, cat_slug, post_slug):
  cat = get_object_or_404(Category, cat_slug=cat_slug)
  post = get_object_or_404(Post, post_slug=post_slug)
  return render(request, 'single.html', {'cat': cat, 'post': post})

@require_POST
def change_language(request):
    language = request.POST.get("language")
    if language:
      activate(language)
      translation.activate(language)
      request.session[translation.LANGUAGE_SESSION_KEY] = language
      return JsonResponse({"success": True, "language": get_language()})
    return JsonResponse({"success": False})