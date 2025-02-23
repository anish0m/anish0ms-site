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
      Mountain hiking is an experience like no other, offering breathtaking views that stretch as far as the eye can see. As you ascend higher, the air grows crisper, filling your lungs with a refreshing purity that city life often lacks. The endless sky above, painted in hues of blue and gold, creates a mesmerizing backdrop to the rugged trails below. Each step forward brings a sense of accomplishment, a connection to nature that reminds you of the vast beauty of the world. Whether hiking alone or with companions, the journey upward becomes as rewarding as the destination itself.

      The appeal of mountain hiking lies not only in the visual splendor but also in the physical challenge. Trails range from gentle slopes to steep, rocky paths that demand endurance and skill. Every climb tests your strength, pushing you beyond limits you once believed were fixed. The uneven terrain, shifting underfoot, requires careful navigation, making each successful step a small victory. Yet, with every effort exerted, the reward is immense—a panoramic view that makes the struggle seem insignificant. The feeling of standing at the summit, gazing down at the valleys below, is an achievement that few experiences can rival.

      Beyond the physical challenge, mountain hiking offers a deep sense of adventure and discovery. Along the way, hikers encounter hidden waterfalls, alpine meadows, and wildlife thriving in the untouched wilderness. The unpredictable nature of the mountains keeps the journey exciting, as weather conditions can shift suddenly, turning a sunny trail into a misty, surreal landscape. These ever-changing elements add to the thrill, making each hike a unique experience. Even well-trodden trails feel different with each visit, as the mountains have a way of revealing new wonders with every step.

      Perhaps the most profound aspect of mountain hiking is the peace it brings. Away from the noise and distractions of daily life, the mountains provide a sanctuary for the mind and soul. The rhythmic crunch of boots against the earth, the whisper of the wind through the trees, and the distant call of birds create a meditative atmosphere. In those quiet moments, standing amidst towering peaks, you realize the insignificance of worldly worries and embrace the pure, unfiltered joy of being present. It is this feeling—this connection to nature—that makes mountain hiking an unforgettable and deeply fulfilling experience.
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
      Programming is a fascinating world where logic meets creativity, but every coder has faced the frustration of elusive errors. Hours can slip away while hunting for that one bug that refuses to reveal itself, making programmers question their sanity. Yet, it's this challenge that keeps the field exciting—solving errors feels like cracking a puzzle, bringing a sense of triumph when the issue is finally resolved. However, some rare errors are so bizarre that even experienced developers struggle to believe they exist. These errors defy expectations, teaching valuable lessons while leaving coders in awe of how unpredictable programming can be.

      One of the most infamous errors is the "Off-by-One" bug, a mistake so small yet so impactful. It happens when loops run one time too many or too few, leading to unexpected behaviors like missing data or infinite loops. A simple misplacement of <= instead of < can cause an entire program to break. In competitive programming, this mistake can mean the difference between an accepted solution and a frustrating failure. What makes this error especially tricky is that the code often looks perfectly fine, making it one of the hardest bugs to spot at a glance.

      Another mind-boggling issue is the Phantom Variable bug, where a variable mysteriously holds a value that was never assigned. This often results from memory corruption, uninitialized variables, or even compiler optimizations that behave unexpectedly. Imagine debugging for hours, only to find out that an array’s out-of-bounds access modified a completely unrelated variable. These unpredictable errors often require stepping through assembly code or deep-diving into memory management to understand what’s really happening.

      Then there’s the dreaded Heisenbug, an error that disappears when you try to debug it. Named after the Heisenberg Uncertainty Principle, these bugs occur due to race conditions, compiler optimizations, or timing issues in multi-threaded programs. When running the program normally, it crashes. But when adding print statements or using a debugger, it suddenly works fine! These bugs can drive developers to the brink of madness, making them question if the error was ever real in the first place.

      Despite the frustration, these head-scratching errors make programming great. They push developers to think critically, learn deeply, and develop patience. Every strange bug is a lesson in how computers actually work beneath the surface, reminding us that even the most logical systems have quirks. While the process of debugging can be exhausting, nothing beats the satisfaction of finally fixing an issue and realizing that, despite its challenges, programming remains one of the most rewarding fields out there.
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
      Nature has a way of leaving us speechless, and nothing captures its beauty quite like a breathtaking sunset. As the sun dips below the horizon, the sky transforms into a canvas of colors—deep purples, fiery oranges, and soft pinks blending in ways that seem almost unreal. For a moment, time slows down, and all the worries of the day fade into insignificance. The gentle breeze carries a sense of peace, and the world feels perfectly balanced, as if nature itself is reminding us to pause and appreciate its wonders.

      There’s something magical about witnessing a sunset in the right place at the right time. Whether standing on a quiet beach, watching the waves reflect the changing hues, or sitting atop a mountain where the entire sky stretches endlessly, the experience is unforgettable. Even in the middle of a busy city, a sudden burst of golden light piercing through towering buildings can turn an ordinary evening into something extraordinary. Nature doesn’t need grand landscapes to amaze us—sometimes, just a single moment of perfect lighting can make everything feel right.

      Beyond its visual beauty, nature has an incredible way of affecting our emotions. The stillness of a forest, the rhythmic crashing of ocean waves, or the gentle rustling of leaves in the wind can bring a sense of calm unlike anything else. Even the scent of rain on dry earth or the sound of distant thunder can evoke powerful feelings of nostalgia and wonder. In those moments, surrounded by nature’s elements, it becomes clear that the world is far more intricate and beautiful than we often remember.

      Perhaps what makes nature truly special is its unpredictability. No two sunsets are ever the same, no two seasons unfold in identical ways. Nature constantly surprises us, offering beauty in the most unexpected places. Whether it's a field of wildflowers blooming after a storm or a rare sighting of a shooting star on a quiet night, these moments remind us that the world is full of wonders waiting to be noticed. And when we take the time to embrace them, even for just a few seconds, everything feels just right.
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