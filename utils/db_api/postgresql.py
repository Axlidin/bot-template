from typing import Union
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config
import json


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def _init_connection(self, conn):
        await conn.set_client_encoding('UTF8')  # Bu qator qo'shilgan

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_grShop(self):
        sql = """
        CREATE TABLE IF NOT EXISTS gr_Shop (
        id SERIAL PRIMARY KEY,
        firstname varchar(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_userRegistration(self, firstname, username, telegram_id):
        sql = "INSERT INTO gr_Shop (firstname, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql,  firstname, username, telegram_id,
                                  fetchrow=True)

    async def select_all_grShop(self):
        sql = "SELECT * FROM gr_Shop"
        return await self.execute(sql, fetch=True)

    async def select_userRegistration(self, **kwargs):
        sql = "SELECT * FROM gr_Shop WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_grShop(self):
        sql = "SELECT COUNT(*) FROM gr_Shop"
        return await self.execute(sql, fetchval=True)

    async def check_tg_id(self, tg_id):
        sql = "SELECT * FROM gr_Shop WHERE telegram_id=$1"
        return await self.execute(sql,tg_id, fetchrow=True)

    async def delete_grShop(self):
        await self.execute("DELETE FROM gr_Shop WHERE TRUE", execute=True)

    async def drop_grShop(self):
        await self.execute("DROP TABLE gr_Shop", execute=True)

    async def see_grShop(self, tg_id):
        sql = "SELECT * FROM gr_Shop WHERE telegram_id=$1"
        return await self.execute(sql, tg_id, fetch=True)

    ##gr_products

    async def create_table_gr_products(self):
        sql = """
        CREATE TABLE IF NOT EXISTS gr_products (
        id SERIAL PRIMARY KEY,

        -- Mahsulot kategoriyasi
        category_code VARCHAR(20) NOT NULL,
        category_name VARCHAR(50) NOT NULL,

        -- Mahsulot kategoriya ichida ketgoriyasi ("Go'sht"->"Mol go'shti")
        subcategory_code VARCHAR(20) NOT NULL,
        subcategory_name VARCHAR(50) NOT NULL,

        -- Mahsulot haqida malumot
        productname VARCHAR(50) NOT NULL,
        photo_url varchar(255) NULL,
        photo_file_id varchar(255) NULL,
        price INT NOT NULL,
        description VARCHAR(3000) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_product(
            self,
            category_code,
            category_name,
            subcategory_code,
            subcategory_name,
            productname,
            photo_url=None,
            photo_file_id=None,
            price=None,
            description="",
    ):
        sql = "INSERT INTO gr_products (category_code, category_name, subcategory_code, subcategory_name, productname, photo_url, photo_file_id, price, description) " \
              "VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9) returning *"
        return await self.execute(
            sql,
            category_code,
            category_name,
            subcategory_code,
            subcategory_name,
            productname,
            photo_url,
            photo_file_id,
            price,
            description,
            fetchrow=True,
        )

    async def get_categories(self):
        sql = "SELECT DISTINCT category_name, category_code FROM gr_products"
        return await self.execute(sql, fetch=True)

    async def get_subcategories(self, category_code):
        sql = f"SELECT DISTINCT subcategory_name, subcategory_code FROM gr_products WHERE category_code='{category_code}'"
        return await self.execute(sql, fetch=True)

    async def count_gr_products(self, category_code, subcategory_code=None):
        if subcategory_code:
            sql = f"SELECT COUNT(*) FROM gr_products WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
        else:
            sql = f"SELECT COUNT(*) FROM gr_products WHERE category_code='{category_code}'"
        return await self.execute(sql, fetchval=True)

    async def get_gr_products(self, category_code, subcategory_code):
        sql = f"SELECT * FROM gr_products WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
        return await self.execute(sql, fetch=True)

    async def get_product(self, product_id):
        sql = f"SELECT * FROM gr_products WHERE id={product_id}"
        return await self.execute(sql, fetchrow=True)

    async def del_gr_products(self, product_id):
        sql = f"DELETE FROM gr_products WHERE id={product_id}"
        return await self.execute(sql, execute=True)

    async def drop_gr_products(self):
        await self.execute("DROP TABLE gr_products", execute=True)
