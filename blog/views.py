from django.shortcuts import render

all_posts = [
    {
        "slug": "hiking on mountains",
        "image": "mountain.jpg",
        "author": "Faaiz Ali Tariq",
        "excerpt": "THere's nothing like Hiking on mountains",
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
        """,
    },
    {
        "slug": "Computer Programming",
        "image": "person.jpg",
        "author": "Faaiz Ali",
        "excerpt": "THere's nothing like Programming",
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
        """,
    },
    {
        "slug": "hiking on mountains",
        "image": "mountain.jpg",
        "author": "Faaiz Ali Tariq",
        "excerpt": "THere's nothing like Hiking on mountains",
        "content": """
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum laborum necessitatibus repudiandae? Quibusdam ad eveniet ipsum adipisci est distinctio quisquam autem, ipsam architecto tempore. Eum reprehenderit veniam maxime voluptatibus voluptatum!
        """,
    }
]


# Create your views here.

def index(request):
    lastest_posts = all_posts[-3:]
    return render(request, 'blog/index.html', {
        "Posts": lastest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')