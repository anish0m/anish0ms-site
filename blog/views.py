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
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "programming-is-fun",
    "image": "coding.jpg",
    "author": "anish0m",
    "date": date(2024, 9, 1),
    "title": "Programming is Great!",
    "excerpt": """Did you ever spend hours searching that one error in code? 
      Take a look at some rare, head-scratching errors you won’t believe exist!
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "into-the-woods",
    "image": "woods.jpg",
    "author": "anish0m",
    "date": date(2013, 3, 15),
    "title": "Nature at its Best",
    "excerpt": """Nature truly is beyond amazing! 
      When the sunset painted the sky in colors you didn’t know existed, and for a moment, everything felt just right.
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "planet-pluto",
    "image": "pluto.jpg",
    "author": "anish0m",
    "date": date(2006, 8, 24),
    "title": "Pluto: Our Lost Planet",
    "excerpt": """Kicked out of the planetary club, Pluto still holds secrets that make it mysterious and captivating. 
      Why does this icy world continue to challenge everything we thought we knew?
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "programming-job-hunt",
    "image": "programmer.jpg",
    "author": "anish0m",
    "date": date(2024, 6, 28),
    "title": "Job Hunting as a Programmer",
    "excerpt": """Job-hunt can be daunting, but as a CSE graduate, you're equipped with in-demand skills. 
      With the right strategy, you're one step closer to unlocking endless career opportunities.
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "my-episode-story",
    "image": "episode.jpg",
    "author": "anish0m",
    "date": date(2013, 7, 11),
    "title": "My First Episode Story",
    "excerpt": """Crafting your first interactive story is an exciting rollercoaster! 
      From developing characters to shaping plot twists, every decision opens a new world for readers to explore.
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "iaac-suggestions",
    "image": "iaac.jpg",
    "author": "anish0m",
    "date": date(2021, 6, 29),
    "title": "International Astronomy and Astrophysics Competition",
    "excerpt": """The IAAC isn’t just a competition; it’s a challenge to test your knowledge and problem-solving skills. 
      Ready to take on the mysteries of the universe and prove your stellar abilities?
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "iymc-suggestions",
    "image": "iymc.jpg",
    "author": "anish0m",
    "date": date(2022, 10, 16),
    "title": "International Youth Math Challenge",
    "excerpt": """The IYMC is more than just a competition – it’s where the brightest young minds take on mind-bending puzzles. 
      Ready to prove your math genius and rise to the top globally?
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
    """
  },
  {
    "slug": "hidden-planet-nine",
    "image": "planet_nine.jpg",
    "author": "anish0m",
    "date": date(2014, 3, 29),
    "title": "Planet Nine: The Hidden Giant",
    "excerpt": """For years, scientists have been searching for a mysterious, unseen planet lurking beyond Neptune. 
      Could Planet Nine be the missing piece that changes our understanding of the solar system?
    """,
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero velit ex cupiditate maxime cum repellendus eligendi delectus, fuga possimus nobis atque odio, sequi doloremque voluptatum aliquid illum a, temporibus itaque.
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
  identified_post = next(post for post in all_posts if post['slug']==slug)
  return render(request, "blog/post-detail.html", {
    "post": identified_post
  })