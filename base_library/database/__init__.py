from base_library.database.database import init_connection, destroy_connection
from base_library.database.database import ...
from sqlalchemy import ext

orm_base = ext.declarative.declarative_base()