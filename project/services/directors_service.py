class DirectorService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, did):
        self.dao.delete(did)
