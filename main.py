from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from uuid import uuid4

from database import Base, SaleModel, engine

class SaleIn(BaseModel):
    name : str
    price : float

class SaleOut(BaseModel):
    id : str | None = None
    name : str
    price : float

app = FastAPI()


def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/sales/{sale_id}")
def get_sale(sale_id :str, db : Session = Depends(get_db)):
    sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if sale is None:
        raise HTTPException (status_code = 404, detail= "sale not found!")
    return sale

class SaleUpdate(BaseModel):
    name : str | None = None
    price : float | None = None


@app.put("/sales/{sale_id}")
def update_sale(sale_id : str, update : SaleUpdate, db: Session = Depends(get_db)):
    sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if sale is None:
        raise HTTPException(status_code = 404, detail = "sale not found!")
    if update.name is not None:
        sale.name = update.name
    if update.price is not None:
        sale.price = update.price
    db.commit()
    db.refresh(sale)
    return sale

@app.delete("/sales/{sale_id}", status_code = 204)
def delete_sale(sale_id: str, db : Session = Depends(get_db)):
    sale = db.query(SaleModel).filter(SaleModel.id == sale_id).first()
    if sale is None:
        raise HTTPException(status_code = 404, detail = "sale not found!")
    db.delete(sale)
    db.commit()
    return


@app.post("/sales", status_code = 201)
def create_sale(sale: SaleIn, db : Session = Depends(get_db)):
    new_sale = SaleModel(id=str(uuid4()), name = sale.name, price = sale.price)
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale
   
@app.get("/sales")
def sale_history(db : Session = Depends(get_db)):
    return db.query(SaleModel).all()

