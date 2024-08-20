# from fastapi import APIRouter, HTTPException
# from app.api.v1.schemas.user import User, UserCreate
# from app.api.v1.services.user_service import create_user, get_user

# router = APIRouter()

# @router.post("/", response_model=User)
# async def create_user_endpoint(user: UserCreate):
#     return await create_user(user)

# @router.get("/{user_id}", response_model=User)
# async def get_user_endpoint(user_id: int):
#     user = await get_user(user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
