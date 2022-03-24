from sqlalchemy import MetaData, Table, Column, String, Integer, create_engine
from sqlalchemy import Text, DateTime, Boolean, select, insert, update, delete, or_, and_

connection_string ="sqlite:///ITEquipments.sqlite"
engine = create_engine(connection_string, echo=False)

metadata = MetaData()
computers = Table('Computer', metadata,
                  Column('Id', Integer(), primary_key=True),
                  Column('Year', Integer()),
                  Column('Price', Integer()),
                  Column('Owner', String(100))
)

metadata.create_all(engine)

def show_metadata():
    for t in metadata.sorted_tables:
        print(f"Table {t.name}:")
        for c in t.columns:
            print(f"{c} ({c.type})")

def do_insert():
    stmt = computers.insert().values(
        Year= 2020,
        Price=25000000,
        Owner='Hoang Pham'
    )
    new_id = 0
    with engine.connect() as con:
        result = con.execute(stmt)
        new_id = result.inserted_primary_key['Id']
        print(f"New ID: {new_id}")
    return new_id

def select_by_id(id):
    stmt = computers.select().where(computers.c.Id == id)
    with engine.connect() as con:
        result = con.execute(stmt).first()
        if result:
            print(result)
        else:
            print(f"no roW found with Id =={id}")

def do_update(id):
    stmt = computers.update().values(
        Year= 2021
    ).where(computers.c.Id == id)

    with engine.connect() as con:
        con.execute(stmt)

def do_delete(id):
    stmt = computers.delete().where(computers.c.Id == id)

    with engine.connect() as con:
        con.execute(stmt)

def statement_infos():
    stmt = computers.select(computers.c.Year, computers.c.Price).where(computers.c.Id == 30)
    print(f"Find computer with ID=30: \n{str(stmt)}")
    print(f"\nparams: \n{str(stmt.compile().params)}")

if __name__=='__main__':
    print("----- show_metadata() ----")
    show_metadata()

    print("----- do_insert() ----")
    id= do_insert()

    print("----- select_by_id) ----")
    select_by_id(id)

    print("----- do_update() ----")
    do_update(id)
    select_by_id(id)

    # print("----- do_delete() ----")
    # do_delete(id)
    # select_by_id(id)

    print("----- END ----")
