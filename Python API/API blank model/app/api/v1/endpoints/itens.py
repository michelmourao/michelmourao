# from fastapi import APIRouter, HTTPException
# from app.api.v1.schemas.item import Item, ItemCreate
# from app.api.v1.services.item_service import create_item, get_item

# router = APIRouter()

# @router.post("/", response_model=Item)
# async def create_item_endpoint(item: ItemCreate):
#     return await create_item(item)

# @router.get("/{item_id}", response_model=Item)
# async def get_item_endpoint(item_id: int):
#     item = await get_item(item_id)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item
