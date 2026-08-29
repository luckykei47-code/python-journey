import json
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

class Sale(BaseModel):
    id : str | None = None
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

@app.get("/sales/{sale_id}")
def get_sale(sale_id : str):
    for sale in sales_history:
        if sale_id == sale_id:
            return sale
        return{"error" : "sale not found!"}


class SaleUpdate(BaseModel):
    name : str | None = None
    price : float | None = None


@app.put("/sales/{sale_id}")
def sale_update(sale_id : str, update : SaleUpdate):
    for sale in sales_history:
        if sale_id == sale_id:
            if update.name is not None:
                sale.name = update.name
            if update.price is not None:
                sale.price = update.price
            save_sales()
            return sale
        return {"error" : "sale not found!"}


@app.delete("/sales/{sale_id}")
def delete_sale(sale_id: str):
    for index, sale in enumerate(sales_history):
        if sale_id == sale_id:
            sales_history.pop(index)
            save_sales()
            return{"message" : "sale deleted."}
        return {"error" : "sale not found!"}

@app.post("/sales")
def create_sale(sale: Sale):
    sale.id = str(uuid4())
    sales_history.append(sale)
    save_sales()
    return sale

@app.get("/sales")
def sale_history():
    return sales_history

