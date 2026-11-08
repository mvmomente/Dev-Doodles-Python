from sqlalchemy import select
from database.connection import engine, SessionLocal
from database.base import Base

from models.user import User
from services.user import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user
)

Base.metadata.create_all(bind=engine)

def main():
    session = SessionLocal()

    try:
        # CREATE
        user = create_user(
            session,
            "Carlos",
            "carlos@email.com",
            "senhacarlos"
        )

        print("Cadastrado:", user.name)

        # READ
        users = get_users(session)

        for u in users:
            print(u.id, u.name, u.email)

        # GET BY ID
        user_found = get_user_by_id(
            session,
            user.id
        )

        print("Encontrado:", user_found.name)

        # UPDATE
        update = update_user(
            session,
            user.id,
            "Carlos Silva"
        )

        print("Atualizado:", update.name)

        # DELTE
        delete = delete_user(
            session,
            user.id
        )

        print("Excluido:", delete)

    finally:
        session.close()

if __name__ == "__main__":
    main()