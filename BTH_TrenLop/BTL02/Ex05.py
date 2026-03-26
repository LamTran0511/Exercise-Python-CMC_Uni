class user:
    def __init__(self,id):
        self.id = id

    @property
    def id(self):
        return self._id
u = user(1)
print(u.id)