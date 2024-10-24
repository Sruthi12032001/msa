from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import model, schemas, auth
from app.database import engine, get_db

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/signup")
async def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.email == user.emailId).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = auth.hash_password(user.password)

    new_user = model.User(
        first_name=user.firstName,
        last_name=user.lastName,
        age=user.age,
        email=user.emailId,
        hashed_password=hashed_password,
        address=user.address,
        state=user.state,
        pin_code=user.pinCode
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "User created successfully"}

@app.post("/login")
async def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.email == user.emailId).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"msg": "Login successful", "user": db_user.email}
