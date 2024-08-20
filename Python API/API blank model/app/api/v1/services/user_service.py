# from app.api.v1.models.user import User
# from app.db.session import Session
# from app.api.v1.schemas.user import UserCreate

# async def create_user(user_create: UserCreate):
#     db = Session()
#     user = User(username=user_create.username, email=user_create.email, hashed_password="hashed_password")
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# async def get_user(user_id: int):
#     db = Session()
#     return db.query(User).filter(User.id == user_id).first()
