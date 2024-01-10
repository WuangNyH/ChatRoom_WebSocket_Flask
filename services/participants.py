from models.participants import Participants
from core.Database import SessionLocal


class ParticipantService:
    def __init__(self):
        self.db = SessionLocal()

    def create_participant(self, name, code_room):
        participant = Participants(username=name, code_room=code_room)
        participants = self.db.query(Participants).filter(Participants.code_room == code_room, Participants.username == name).all()

        if len(participants) != 0:
            return participant

        self.db.add(participant)
        self.db.commit()
        self.db.refresh(participant)
        self.db.close()
        return participant
