from datetime import date
from django.shortcuts import render

all_posts = [
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "anish0m",
    "date": date(2017, 7, 13),
    "title": "Mountain Hiking",
    "excerpt": """There's nothing like the views you get when hiking in the mountains! 
      The crisp air, the endless sky, and the sense of adventure make every step worth it!
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "programming-is-fun",
    "image": "coding.jpg",
    "author": "anish0m",
    "date": date(2024, 9, 1),
    "title": "Programming is Great!",
    "excerpt": """
      Did you ever spend hours searching that one error in your code? 
      Take a look at some rare, head-scratching errors you won’t believe exist!
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "into-the-woods",
    "image": "woods.jpg",
    "author": "anish0m",
    "date": date(2013, 3, 15),
    "title": "Nature at its Best",
    "excerpt": """
      Nature truly is beyond amazing! 
      When the sunset painted the sky in colors you didn’t know existed, 
      and for a moment, everything felt just right.
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex
      cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis
      atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  }
]

def get_date(post):
  return post.get('date')

# Create your views here.

def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html", {
    "posts": latest_posts
  })

def posts(request):
  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })

def post_detail(request, slug):
  return render(request, "blog/post-detail.html")