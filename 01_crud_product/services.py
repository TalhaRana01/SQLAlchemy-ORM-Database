from models import User, Post
from database import SessionLocal
from sqlalchemy import select



# Create a User

def create_user(name: str, email:str):
  with SessionLocal() as session:
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
  

# Create Post
def create_post(user_id: int, title: str, content:str):
  with SessionLocal() as session:
    post = Post(user_id=user_id, title=title, content=content)
    session.add(post)
    session.commit()

# Get All User

def  get_all_user():
  with SessionLocal() as session:
    stmt = select(User)
    users = session.scalar(stmt).all()
    return users
    
# Get Single User
def Get_user_by_id(user_id: int):
  with SessionLocal() as session:
    user = session.get_one(User, user_id)
    return user
  
  
# Update User email

def update_user_email(user_id: int, new_email: str):
  with SessionLocal() as session:
    user = session.get(User, user_id)
    if user:
      user.email = new_email
      session.commit()
    return user
  
  
# Get Single Post
def Get_post_by_id(post_id: int):
  with SessionLocal() as session:
    post = session.get_one(Post, post_id)
    return post


# Get all post for a user

def get_posts_by_user(user_id:int):
  with SessionLocal() as session:
    user = session.get(User, user_id)
    posts = user.posts if user else []
    return posts
  
# Delete Post

def delete_post(post_id: int):
  with SessionLocal() as session:
    post = session.get(Post, post_id)
    if post:
      session.delete(post)
      session.commit()
      