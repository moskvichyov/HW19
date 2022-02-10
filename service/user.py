from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    # def get_all(self):
    #     return self.dao.get_all()
    #
    # def create(self, genre_d):
    #     return self.dao.create(genre_d)
    #
    # def update(self, genre_d):
    #     self.dao.update(genre_d)
    #     return self.dao
    #
    # def delete(self, rid):
    #     self.dao.delete(rid)
