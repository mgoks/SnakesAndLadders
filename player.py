class Player:
    def __init__(self, id):
        self.id = id
        self.position = 0

    def move(self, i):
        """
        Move player to square i
        """
        self.position = i

    def __repr__(self): return f'Player {self.id}'
