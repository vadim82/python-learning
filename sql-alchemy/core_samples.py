# Have to install psycopg2
# The prerequisite is the postgres dev lib
# sudo apt install libpq-dev

from pprint import pprint
from sqlalchemy import create_engine, Table, MetaData, Column
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.schema import Column, MetaData
from sqlalchemy.sql.sqltypes import TIMESTAMP, Integer, String
from sqlalchemy.sql import select

connection_string = "postgresql://postgres:test@localhost:5432/dvdrental"
engine = create_engine(connection_string)

# conn = engine.connect()


actors_meta = MetaData()
actors_table = Table(
    "actor", actors_meta,
    Column("actor_id", Integer, primary_key=True, nullable=False),
    Column("first_name", String(45), nullable=False),
    Column("last_name", String(45), nullable=False),
    Column("last_update", TIMESTAMP(timezone=False), nullable=False),
),


with engine.connect() as conn:
    conn: Connection

    # Basic select from engine
    # query = "select first_name, last_name from actor"
    # results = conn.execute(query)
    # pprint(results.fetchall())

    # basic select using select utility from sql alchemy

    query = select(actors_table)
    cursor = conn.execute(query)
    result = cursor.fetchall()
    pprint(result)
