# Have to install psycopg2
# The prerequisite is the postgres dev lib
# sudo apt install libpq-dev

from pprint import pprint
from sqlalchemy import create_engine, Table, MetaData, Column, func
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.schema import Column, MetaData
from sqlalchemy.sql.sqltypes import TIMESTAMP, Integer, String
from sqlalchemy.sql import expression, select

connection_string = "postgresql://postgres:test@localhost:5432/dvdrental"
engine = create_engine(connection_string)

# conn = engine.connect()


metadata = MetaData()
actors_table = Table(
    "actor", metadata,
    Column("actor_id", Integer, primary_key=True, nullable=False),
    Column("first_name", String(45), nullable=False),
    Column("last_name", String(45), nullable=False),
    Column("last_update", TIMESTAMP(timezone=False), nullable=False),
)


with engine.connect() as conn:
    conn: Connection

    # Basic select from engine
    # query = "select first_name, last_name from actor"
    # results = conn.execute(query)
    # pprint(results.fetchall())

    # basic select using select utility from sql alchemy

    # query = select(actors_table)
    # cursor = conn.execute(query)
    # result = cursor.fetchall()
    # pprint(result)

    print(f"{actors_table.c.first_name!r}")
    expr = actors_table.columns.actor_id > 5
    print(expr.compile().params)


    # 'or' and 'and' operators are '|' and '&'
    # equality is '==' operator
    # keep in mind that postgres is case sensitive! so you have to be careful when you query
    q = select(actors_table) \
        .where(actors_table.c.first_name.startswith('A')) \
        .order_by(actors_table.c.last_name.desc()) \
        .offset(5) \
        .limit(5)
    pprint(conn.execute(q).fetchall())


    agg1 = select(func.sum(actors_table.c.actor_id))
    print(conn.execute(agg1).scalar())



