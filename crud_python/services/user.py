from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.user import User

def create_user(
        session: Session,
        name: str,
        email: str,
        password: str
):
    user = User(
        name=name,
        email=email,
        password=password
    )

    try:
        session.add(user)
        session.commit()
        session.refresh(user)

        return user
    except IntegrityError:
        session.rollback()
        print("Este e-mail já está cadastrado")
        raise

def get_users(session: Session):
    command = select(User).order_by(
        User.id.asc()
    )

    return session.scalars(command).all()

def get_user_by_id(
        session: Session,
        user_id: int
):
    return session.get(User, user_id)

def update_user(
        session: Session,
        user_id: int,
        name: str
):
    user = session.get(User, user_id)

    if user is None:
        return None

    try:
        user.name = name

        session.commit()
        session.refresh(user)

        return user
    except Exception:
        session.rollback()
        raise

def delete_user(
        session: Session,
        user_id: int
):
    user = session.get(User, user_id)

    if user is None:
        return False

    try:
        session.delete(user)
        session.commit()

        return True
    except Exception:
        session.rollback()
        raise