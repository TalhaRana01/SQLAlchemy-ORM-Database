from models import User, Post
from database import SessionLocal



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
    
    
# Get Single User
def Get_user_by_id(user_id: int):
  with SessionLocal() as session:
    user = session.get_one(User, user_id)
    return user
    