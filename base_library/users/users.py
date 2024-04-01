import sqlalchemy as sql
from sqlalchemy.dialects import postgresql
from sqlalchemy import ext
from base_library import database
import uuid
import bcrypt

class User(database.orm_base):
    __tablename__ = 'users'
    
    user_id = sql.Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()
    )

    username = sql.Column(sql.VARCHAR(40), nullable=False)
    email = sql.Column(sql.VARCHAR(255), nullable=False)
    hashed_password = sql.Column(sql.VARCHAR(255), nullable=False)
    
    async def set_password(
        self, plain_password: str, db: ext.asyncio.AsyncSession
    ) -> str:
        hashed_password = bcrypt.hashpw(plain_password, bcrypt.gensalt())
        self.hashed_password = hashed_password
        db.add(self)
        db.commit()
        return hashed_password
        
        
        
        
        
        