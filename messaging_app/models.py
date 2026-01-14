from sqlalchemy import Column, Integer, String, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, index=True)      # Who sent it?
    recipient = Column(String, index=True)   # Who is it for?
    content = Column(String)                 # The actual message body
    is_read = Column(Boolean, default=False) # Has the recipient seen it?
    timestamp = Column(DateTime, default=datetime.utcnow) # When was it sent?

# Database Setup (Same efficient pattern as Notes App)
DATABASE_URL = "sqlite:///./messages.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("✅ Messaging Database Initialized!")