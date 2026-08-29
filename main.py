import json
from fastapi import FastAPI
from pydantic import BaseModel


class Sale(BaseModel):
    name : str
    price : float

app = FastAPI()


def load_sales():
    try:
        with open("sales.json", "r") as file:
            data = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return []
    loaded = []
    for item in data:
        loaded.append(Sale(**item))
    return loaded


def save_sales():
    data = []
    for sale in sales_history:
        data.append(sale.model_dump())
    with open("sales.json", "w") as file:
        json.dump(data, file, indent=4)

sales_history = load_sales()


@app.post("/sales")
def create_sale(sale: Sale):
    sales_history.append(sale)
    save_sales()
    return sale

@app.get("/sales")
def sale_history():
    return sales_history





















































    # @app.get("/")
# def read_root():
#     return{"message" : "Hello, World!"} 

# @app.get("/greet/{name}")
# def greet(name : str, excited : bool = False):
#     if excited:
#         return{"message" : f"HELLO {name}!!!"}
#     return{"message" : f"Hello {name}!"}