import asyncio
from app.database.database import engine, Base


from app.database.models.users import User
from app.database.models.messages import Messages
from app.database.models.images import Images


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_tables())
    print("Table Created")