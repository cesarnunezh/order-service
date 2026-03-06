import uvicorn

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .database import get_db
from .models import Order, Product

app = FastAPI(title="order-api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class OrderCreate(BaseModel):
    product_id: int = Field(..., ge=1)
    quantity: int = Field(..., ge=1)


class OrderStatusUpdate(BaseModel):
    status: str = Field(..., min_length=1, max_length=32)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.post("/orders", status_code=201)
async def create_order(payload: OrderCreate, db: AsyncSession = Depends(get_db)):
    # Get product from DB
    result = await db.execute(select(Product).where(Product.id == payload.product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    new_order = Order(
        product_id=payload.product_id,
        quantity=payload.quantity,
        status="pending",
    )

    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    return new_order


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000)
