from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get("/")
async def hello():
    return {"massage": "Привіт, світ!"}


@app.get("/items/{item_id}")
def get_detail(
        item_id: int = Path(..., title="ID", description="Це ідентифікатор користувача")
) -> dict:
    return {"items": [item_id]}


@app.get("/items/")
async def return_items(
        q: Optional[int] = Query(None, title="Пошуковий запит", description="Фільтрація елементів")
) -> list[int]:
    list_items = [2, 4, 6, 66, 77, 9]
    if q is not None:
        list_items = [x for x in list_items if x == q]
    list_items.sort()
    return list_items


@app.post("/items/add")
async def add_item(
            name: str = Query(..., title="Ім'я нового користувача"),
            description: Optional[str] = Query(None, title="Опис нового  елементу")
    ):
    list = []
#    Не знаю що далі


@app.get("/users/{user_id}")
async def read_user(
        user_id: int = Path(..., title="ID користувача", description="Це ідентифікатор користувача"),

) -> dict:
    return {"user": [user_id]}


@app.get("/users/")
async def get_users():
    users = ["Dima", "Diana"]
    return users


@app.post("/users/add")
async def add_user(
    name: str = Query(..., title="Ім'я нового користувача"),
    email: Optional[str] = Query(None, title="Email нового користувача")
) -> dict:
    users = [{"id": 1, "name": "Dima", "email": "dima@example.com"}]
    new_id = users + 1
    new_user = {"id": new_id, "name": name, "email": email}
    users.append(new_user)
    return new_user


@app.get("/orders/{order_id}")
async def get_order(order_id: int = Path(..., title="Ідентифікатор замовлення")
) -> dict:
    return {"order_id": order_id}