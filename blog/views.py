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
    "date": date(2015, 7, 31),
    "title": "Pluto: Our Lost Planet",
    "excerpt": """Kicked out of the planetary club, Pluto still holds secrets that make it mysterious and captivating. 
      Why does this icy world continue to challenge everything we thought we knew?
    """,
    "content": """
      Pluto was once the ninth planet of our solar system, a small yet significant member of the planetary family. However, in 2006, the International Astronomical Union (IAU) redefined what it means to be a planet, and Pluto was reclassified as a "dwarf planet." This decision sparked heated debates among scientists and space enthusiasts alike. Many argued that Pluto deserved its planetary status, while others supported the scientific reasoning behind its reclassification. Despite being kicked out of the planetary club, Pluto remains one of the most fascinating celestial bodies, continuing to challenge our understanding of the solar system.

      One of the most mysterious aspects of Pluto is its composition and atmosphere. Unlike the gas giants or rocky planets, Pluto is a world of ice and rock, with a surface covered in frozen nitrogen, methane, and carbon monoxide. Its atmosphere is thin but dynamic, expanding and collapsing as Pluto moves along its elliptical orbit. The discovery of towering ice mountains and vast, smooth plains by NASA’s New Horizons mission in 2015 shattered previous assumptions about Pluto being a static, lifeless rock. Instead, Pluto appears to be geologically active, raising questions about what powers such activity in an object so far from the Sun.

      Pluto's largest moon, Charon, adds another layer of intrigue. Charon is so large relative to Pluto that the two bodies orbit a common center of gravity, making them more of a binary system than a traditional planet-moon relationship. This unique setup challenges our understanding of celestial mechanics and raises questions about how such a system formed. Some scientists believe that a massive collision early in the solar system’s history created Charon, much like how Earth’s Moon was formed. The deep canyons and geological features on Charon also suggest a complex history that we are only beginning to understand.

      Despite its demotion, Pluto remains a key to unlocking the secrets of the Kuiper Belt—a vast region beyond Neptune filled with icy bodies and remnants from the early solar system. Studying Pluto helps scientists understand the formation of planets, the evolution of atmospheres, and even the potential for hidden oceans beneath icy exteriors. Some researchers speculate that beneath Pluto’s icy shell, a subsurface ocean might exist, kept warm by internal heat. If true, this would raise exciting possibilities about the potential for microbial life in places we least expect.

      Pluto may no longer be classified as a planet, but its mysteries continue to captivate astronomers and space enthusiasts. It challenges our understanding of planetary science, reminding us that space is full of surprises. The debate over its classification lingers, but perhaps what truly matters is not whether Pluto is a planet, but what it can teach us about the universe. As space exploration advances, future missions may one day reveal even more secrets about this icy world, proving that Pluto is far from forgotten.
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
      Job hunting can be an overwhelming process, especially in the competitive world of programming. As a Computer Science graduate, you possess skills that are highly sought after, but landing the right job requires more than just technical knowledge. The hiring landscape is constantly evolving, and companies look for candidates who not only excel in coding but also demonstrate problem-solving abilities, adaptability, and strong communication skills. While the journey might seem daunting, with the right strategy, you can navigate through the challenges and secure a rewarding position in the tech industry.

      The first step to a successful job hunt is building a solid resume and online presence. Your resume should highlight your technical skills, programming languages, and projects that showcase your expertise. However, in today’s digital era, having a strong LinkedIn profile and an active GitHub or portfolio website can significantly boost your chances. Recruiters often look at GitHub repositories to assess coding practices and problem-solving approaches. Contributing to open-source projects or maintaining personal projects demonstrates initiative and a passion for learning, making you stand out from the crowd.

      Networking is another crucial aspect of job hunting. Many programming jobs are filled through referrals rather than job postings. Attending hackathons, tech conferences, and meetups can help you connect with industry professionals and potential employers. Engaging in online communities such as Stack Overflow, Reddit’s programming forums, or Discord groups can also lead to unexpected job opportunities. Reaching out to professionals on LinkedIn with a personalized message can sometimes open doors to opportunities that aren’t advertised publicly. Building connections in the industry can be as valuable as having technical expertise.
      
      Acing technical interviews is a major challenge for programmers. Most companies conduct multiple rounds, including coding tests, system design interviews, and behavioral assessments. Preparing for these requires consistent practice. Platforms like LeetCode, Codeforces, and HackerRank help sharpen problem-solving skills, while mock interviews with peers or on websites like Pramp can build confidence. Understanding data structures, algorithms, and system design principles is crucial, but so is the ability to explain your thought process clearly. Communication plays a vital role in technical interviews, as employers want to see how well you approach problems and collaborate with teams.

      Soft skills are often overlooked but are just as important as technical proficiency. Employers seek candidates who can work well in teams, adapt to new technologies, and communicate effectively. Writing clean, maintainable code and explaining it in a simple manner is a valuable skill. Additionally, problem-solving in real-world scenarios often involves collaborating with designers, product managers, and other developers. Demonstrating teamwork, time management, and the ability to handle constructive criticism can set you apart from other candidates.

      Job hunting as a programmer may seem intimidating, but with a structured approach, it becomes a rewarding journey. By strengthening your technical and soft skills, networking with professionals, and preparing for interviews, you increase your chances of landing the right job. The tech industry is vast, offering endless opportunities in fields like web development, data science, cybersecurity, and artificial intelligence. With persistence and the right mindset, you’re one step closer to unlocking a fulfilling career in programming.
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
      Writing my first interactive story was an experience unlike any other—a mix of creativity, excitement, and plenty of trial and error. The process began with a simple idea, but bringing it to life required careful planning. Choosing the right genre, developing compelling characters, and designing multiple story paths made me appreciate the complexity behind interactive storytelling. Unlike traditional writing, where the plot moves in a single direction, an interactive story demands choices that truly impact the outcome. Every decision the reader makes must feel meaningful, pushing the narrative in exciting and unexpected ways.

      Character development quickly became one of the most engaging parts of the process. In an interactive story, characters aren’t just personalities on a page; they react differently based on the reader’s choices. Crafting relatable, multidimensional characters required thinking beyond just their looks or backstories. I had to ensure they had unique dialogue styles, distinct motivations, and emotional depth. Balancing multiple love interests, rivalries, or friendships while maintaining consistency across different story paths was challenging, but it made the experience feel more real and immersive.

      Plot twists were another thrilling aspect of the journey. Unlike linear stories, interactive plots needed multiple branches, each leading to different consequences. This meant foreshadowing key events while making sure no path felt weaker than the others. I experimented with different scenarios—what if a character betrayed the protagonist? What if the reader’s choices led to an unexpected alliance? Keeping the suspense alive without making the story too predictable or confusing took careful structuring. Testing different choices and seeing how they played out helped refine the pacing and depth of the narrative.

      By the time I finished my first episode story, I realized just how much effort goes into creating an engaging interactive experience. Every detail, from the smallest dialogue choice to major plot developments, shaped the journey for the reader. It was more than just writing—it was world-building, game design, and storytelling combined. Seeing players immerse themselves in the story, eagerly anticipating what would happen next, made all the effort worthwhile. The process was a rollercoaster, but one I would gladly ride again.
    """
  },
  {
    "slug": "iaac-at-a-glance",
    "image": "iaac.jpg",
    "author": "anish0m",
    "date": date(2021, 6, 29),
    "title": "International Astronomy and Astrophysics Competition",
    "excerpt": """The IAAC isn’t just a competition; it’s a challenge to test your knowledge and problem-solving skills. 
      Ready to take on the mysteries of the universe and prove your stellar abilities?
    """,
    "content": """
      The International Astronomy and Astrophysics Competition (IAAC) is a global challenge that attracts students from all over the world, offering them the opportunity to demonstrate their knowledge in the fields of astronomy, astrophysics, and mathematics. The competition is structured to gradually increase in difficulty, with each round pushing participants to apply both theoretical knowledge and problem-solving abilities to complex questions. The contest is completely online, allowing participants from different regions to compete on an equal platform, making it accessible to a wider audience.

      The journey begins with the Qualification Round, where contestants face a set of questions designed to test their understanding of fundamental concepts in astronomy and physics. These problems often require participants to apply basic formulas, understand celestial phenomena, and perform simple calculations related to planetary motions and gravitational forces. The Qualification Round is open-book, but its difficulty lies in the requirement for precise analysis and the ability to connect different concepts, which challenges participants to think critically. Successful completion of this round is a prerequisite for moving forward to the next stage.

      For those who pass the initial round, the Pre-Final Round presents more complex problems, testing deeper knowledge of astrophysics and astronomical observation. Here, participants face stricter time limits, and the problems demand more advanced reasoning, including interpreting astronomical data, solving intricate mathematical equations, and applying theoretical models to real-world space phenomena. The pressure intensifies, and only those with the strongest grasp of the subject move on to the Final Round. This stage of the competition requires not just skill but also the ability to manage time efficiently while solving sophisticated challenges.

      The Final Round is the pinnacle of the IAAC, where the best of the best face the most difficult challenges. The problems in this stage are designed to test the participants' in-depth understanding of astrophysics, advanced mathematical principles, and their ability to synthesize information to solve complex problems. Sometimes the questions include live assessments or involve real data analysis, making the experience even more immersive. The participants’ performance in this round is a direct reflection of their problem-solving capabilities, their creativity in applying scientific principles, and their ability to communicate their thought processes effectively.

      Aside from the intellectual stimulation, IAAC offers significant recognition for its top performers. High-ranking students receive certificates that showcase their excellence in astronomy and astrophysics, and many winners gain access to opportunities such as scholarships, internships, and the chance to have their solutions published in scientific journals. Ultimately, participating in the IAAC is a great way for aspiring astrophysicists and astronomers to put their skills to the test, gain international recognition, and take the next step toward a future in space science.
    """
  },
  {
    "slug": "iymc-at-a-glance",
    "image": "iymc.jpg",
    "author": "anish0m",
    "date": date(2022, 10, 16),
    "title": "International Youth Math Challenge",
    "excerpt": """The IYMC is more than just a competition – it’s where the brightest young minds take on mind-bending puzzles. 
      Ready to prove your math genius and rise to the top globally?
    """,
    "content": """
      The International Youth Math Challenge (IYMC) is a highly regarded global competition that invites young students to put their mathematical skills to the test. It’s designed to challenge participants with a series of increasingly difficult problems in various branches of mathematics, from algebra and geometry to number theory and combinatorics. The competition draws participants from all over the world, providing a platform for them to not only compete but also collaborate with like-minded peers who share a passion for problem-solving.

      The competition begins with the Qualification Round, where participants are presented with a series of questions that cover foundational mathematical concepts. This round tests a broad range of skills, including logical reasoning, basic problem-solving techniques, and the ability to apply known mathematical formulas. The problems are designed to assess a contestant’s understanding of core mathematical principles, but they also require some creative thinking. Those who successfully solve the Qualification Round problems advance to the next stage, based on their performance.

      For those who move on, the Pre-Final Round presents a step-up in complexity. The problems in this round demand a deeper understanding of mathematical theory and the ability to solve more abstract problems. This stage is often time-constrained, pushing participants to think critically and solve problems efficiently under pressure. Some problems might require the use of advanced techniques in algebra, calculus, or combinatorics, while others challenge participants to think outside the box and use mathematical reasoning in novel ways. Only the best performers make it to the Final Round, where the ultimate challenges await.

      The Final Round of the IYMC is where the highest-achieving participants face the most difficult problems of all. These questions require not only deep mathematical knowledge but also advanced problem-solving skills and creativity. Some problems are designed to test participants' ability to formulate mathematical models for real-world scenarios, while others delve into complex theoretical math. The Final Round often includes questions that are open-ended, requiring participants to justify their solutions and demonstrate their reasoning process clearly. This is the ultimate test for the brightest mathematical minds, and only the top scorers are awarded with the prestigious recognition that comes with performing well in the competition.

      The International Youth Math Challenge offers significant rewards and recognition for those who excel. High-ranking participants receive certificates that showcase their accomplishments, with special awards for the highest performers in each age group. These awards are valuable additions to any academic portfolio, especially for students who aspire to pursue careers in mathematics, science, or engineering. Beyond the recognition, the competition opens doors to scholarships, internships, and other opportunities for young mathematicians to further develop their skills and pursue academic excellence.
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