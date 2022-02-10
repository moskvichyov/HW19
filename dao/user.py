from dao.model.user import User
from exception import IncorrectData


class UserDAO:
    def __init__(self, session):
        self.session = session
        self._roles = {'user', 'admin'}

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_by_username(self, username: str):
        return self.session.query(User).filter(username=username).one_or_none()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

    def update_role(self, username: str, role: str):
        if role not in self._roles:
            raise IncorrectData
        user = self.get_by_username(username)
        user.role = role
        self.session.add(user)
        self.session.commit()


    def update(self, username: str, password_hash: str):
        user = self.get_by_username(username)
        user.password = password_hash

        self.session.add(user)
        self.session.commit()
