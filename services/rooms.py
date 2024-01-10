import random
from string import ascii_uppercase

from models.participants import Participants
from models.rooms import Room
from core.Database import SessionLocal


class RoomService:
    def __init__(self):
        self.db = SessionLocal()

    def generate_unique_code(self, length):
        rooms = self.db.query(Room.code_room).all()
        while True:
            code = ""
            for _ in range(length):
                code += random.choice(ascii_uppercase)

            if code not in rooms:
                break

        return code

    def create_room(self, req_data):
        code_room = self.generate_unique_code(4)
        new_room = Room(code_room=code_room, **req_data)
        self.db.add(new_room)
        self.db.commit()
        self.db.refresh(new_room)
        return new_room

    def list_rooms(self, name):
        try:
            rooms = []
            result = self.db.query(Room).join(Participants,
                                              Room.code_room == Participants.code_room).filter(
                Participants.username == name).group_by(Room.code_room).all()

            for room in result:
                rooms.append(self.room_mapping(room))

            return rooms
        finally:
            self.db.close()

    def room_mapping(self, room):
        return dict(
            id=room.id,
            room_name=room.room_name,
            created_at=room.created_at,
            created_by=room.created_by,
            code_room=room.code_room
        )
