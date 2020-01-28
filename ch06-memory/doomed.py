class Doomed:
    def __init__(self,*friends):
        self.friends = list(friends)
        print(f"Created Doomed at {id(self)}")

    def __del__(self):
        print(f"Deleting Doomed at {id(self)}")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Doomed object @ {id(self)} with {len(self.friends)} friends"