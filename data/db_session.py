from data.create import create_user_table, create_game_table, create_movie_table, create_frame_table


async def global_init(db_file: str):
    await create_user_table(db_file)
    await create_movie_table(db_file)
    await create_game_table(db_file)
    await create_frame_table(db_file) # !!!!!