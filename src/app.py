from fastapi import FastAPI, HTTPException
from src.schemas import PostCreate, PostResponse
app = FastAPI()

posts = {
    1: {"title": "The Freezing Paradox", "content": "Hot water can actually freeze faster than cold water under certain conditions, a phenomenon known as the Mpemba effect."},
    2: {"title": "The Mystery of Mona Lisa", "content": "The Mona Lisa has no clearly visible eyebrows because they were likely eroded over centuries of cleaning or were lost during a restoration."},
    3: {"title": "The Shortest Sentence", "content": "'I am' is the shortest complete sentence in the English language, containing both a subject and a predicate."},
    4: {"title": "The Strongest Muscle", "content": "The masseter (jaw muscle) is the strongest muscle in the human body based on its weight, allowing you to bite down with immense force."},
    5: {"title": "Ant Power Naps", "content": "Ants don't sleep like humans; instead, they take many short rest periods totaling about 8 minutes every 12 hours."},
    6: {"title": "Moon Weight", "content": "When the moon is directly overhead, its gravitational pull is strong enough that you will actually weigh slightly less."},
    7: {"title": "The Desert Shield", "content": "Camels have three eyelids to protect their eyes from blowing sand while traveling through harsh desert environments."},
    8: {"title": "Temperature Twinning", "content": "Minus 40 degrees Celsius is the exact same temperature as minus 40 degrees Fahrenheit—the only point where the two scales meet."},
    9: {"title": "Smallest Mammal", "content": "The bumblebee bat is the world's smallest mammal, weighing less than a penny and measuring about an inch long."},
    10: {"title": "Human Eye Colors", "content": "The human eye is capable of distinguishing approximately 10 million different colors thanks to specialized cone cells in the retina."}
}

@app.get("/posts")
def get_posts(limit : int):
    if limit:
        return list(posts.values())[:limit]
    return posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    if id not in posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts.get(post_id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post ={"title": post.title, "content": post.content}
    posts[max(posts.keys())+1] = new_post
    return new_post
