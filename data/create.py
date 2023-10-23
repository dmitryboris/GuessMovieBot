import aiosqlite


async def create_user_table(db_file: str):
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users'
                         '(id INTEGER PRIMARY KEY,'
                         ' name TEXT NOT NULL,'
                         ' count INTEGER)')
        await db.commit()


async def create_movie_table(db_file: str):
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS movies'
                         '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                         ' name TEXT NOT NULL,'
                         ' character TEXT)')
        await db.commit()


async def create_game_table(db_file: str):
    async with aiosqlite.connect(db_file) as db:
        await db.execute('CREATE TABLE IF NOT EXISTS games'
                         '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                         'user_id INTEGER,'
                         '???movie_id INTEGER,'
                         'FOREIGN KEY (user_id) REFERENCES users (id),'
                         '???FOREIGN KEY (mov_id) REFERENCES subscriptions (id))')
        await db.commit()


