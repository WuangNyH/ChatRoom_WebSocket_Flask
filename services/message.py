from models.message import Message
from core.Database import SessionLocal
from models.rooms import Room


class MessageService:
    def __init__(self):
        self.db = SessionLocal()

    def create_message(self, code_room, content, username):
        new_message = Message(code_room=code_room, content=content, username=username)
        self.db.add(new_message)
        self.db.commit()
        self.db.refresh(new_message)
        self.db.close()
        return new_message

    def get_message(self, code_room):
        result = self.db.query(Message).filter_by(code_room=code_room).all()
        list_content = []
        for message in result:
            content = {
                "name": message.username,
                "message": message.content
            }
            list_content.append(content)
        return list_content
