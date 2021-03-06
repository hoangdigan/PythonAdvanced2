import sqlalchemy as sa
import sqlalchemy.orm as orm

from .modelbase import ModelBase


factory = None

def global_init(db_file):
    global factory

    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file!")

    connection_string = 'sqlite:///' + db_file.strip()
    print(f"Connecting to database: {connection_string}")

    engine = sa.create_engine(connection_string, echo=False, connect_args={'check_same_thread': False})
    factory = orm.sessionmaker(bind=engine)
    ModelBase.metadata.create_all(engine)

