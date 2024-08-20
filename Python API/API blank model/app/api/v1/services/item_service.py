# from app.api.v1.models.item import Item
# from app.db.session import Session
# from app.api.v1.schemas.item import ItemCreate

# async def create_item(item_create: ItemCreate):
#     db = Session()
#     item = Item(name=item_create.name, description=item_create.description)
#     db.add(item)
#     db.commit()
#     db.refresh(item)
#     return item

# async def get_item(item_id: int):
#     db = Session()
#     return db.query(Item).filter(Item.id == item_id).first()
