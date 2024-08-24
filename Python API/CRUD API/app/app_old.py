from fastapi import FastAPI
from app.auth import router as auth_router
from datetime import datetime

app = FastAPI()

app.include_router(auth_router)

@app.get("/datetime")
def get_datetime():
    dt = datetime.now()
    return dt


# from app.models import UserCRUD, User
# from app.database import session
# from app.auth import verify_password


# user_crud = UserCRUD(session)
# user = user_crud.read_user(username='NewMike')

# if user is not None:
#     print(f"Usuário encontrado: {user.username}, hash: {user.password_hash}")
#     passhash = user.password_hash
# else:
#     print("Usuário não encontrado")

# session.close()


# passhash = get_password_hash('teste123')
# print(passhash)



#passhash = '$2b$12$5w8zyDUIU6NN7ybMka6gnegJb7x89M5/AtPc04d.unOCbBULY77eC'
# verification = verify_password('teste123', passhash)
# print(f'Verification: {verification}')