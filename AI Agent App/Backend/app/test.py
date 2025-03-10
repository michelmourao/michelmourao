# from models import UserCRUD
# from database import session

# new_user = UserCRUD(session).create_user(email='michelmourao123@gmail.com', name='Michel Mourão', plan='pro', password='12345678')
# session.close()
# print('New user created!')

# user_deleted =UserCRUD(session).delete_user(user_id='3')
# session.close()
# print("Deleted: ", user_deleted)


from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

print(OAuth2PasswordRequestForm)