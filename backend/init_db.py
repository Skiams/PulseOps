"""Create missing tables for local development, before introducing migrations."""

from backend.database import engine
from backend.models import Base


def main() -> None:
    try:
        Base.metadata.create_all(engine)
        print("Database initialized: services table is ready.")
    finally:
        engine.dispose()


if __name__ == "__main__":
    main()
