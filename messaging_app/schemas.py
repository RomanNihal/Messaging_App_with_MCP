from pydantic import BaseModel
from datetime import datetime

# Used when SENDING a message (Input)
class MessageSend(BaseModel):
    sender: str
    recipient: str
    content: str

# Used when READING messages (Output)
class MessageRead(MessageSend):
    id: int
    is_read: bool
    timestamp: datetime

    class Config:
        from_attributes = True