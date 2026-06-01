from sqlmodel import SQLModel, create_engine


engine = create_engine(f"sqlite:///database.db", connect_args={"check_same_thread": False})


def init_db() -> None:
    SQLModel.metadata.create_all(engine)