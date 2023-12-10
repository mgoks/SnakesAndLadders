import random
from player import Player


class SnakesAndLadders:
    BOARD_LEN = 10
    LAST_SQUARE = BOARD_LEN ** 2

    def __init__(self):
        self.board = [0]
        self.players = []
        self.player_index = 0
        for current_square in range(1, SnakesAndLadders.BOARD_LEN ** 2 + 1):
            p = random.random()
            if p < 0.1 and 1 < current_square:  # snake
                self.board.append(random.randrange(1, current_square))
            elif p < 0.2 and current_square + 1 < SnakesAndLadders.BOARD_LEN:
                # ladder
                self.board.append(random.randint(current_square + 1,
                                                 SnakesAndLadders.BOARD_LEN))
            else:
                self.board.append(current_square)
        # Last square can't be a snake or ladder
        self.board[SnakesAndLadders.LAST_SQUARE] = SnakesAndLadders.LAST_SQUARE

    def move_player(self, k):
        """
        Moves current player.
        """
        player = self.current_player()
        if player.position + k > SnakesAndLadders.LAST_SQUARE:
            raise ValueError
        player.move(player.position + k)
        while self.board[player.position] != player.position:
            if self.board[player.position] < player.position:
                special_square = 'snake'
            else:
                special_square = 'ladder'
            print(f"It's a {special_square}. {player} moves to "
                  f"{self.board[player.position]}")
            player.move(self.board[player.position])

    def add_player(self, player):
        self.players.append(player)

    def current_player(self):
        return self.players[self.player_index]

    def winner(self):
        for player in self.players:
            if player.position == SnakesAndLadders.LAST_SQUARE:
                return player
        return None

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    def end_turn(self):
        self.player_index = (self.player_index + 1) % len(self.players)


if __name__ == '__main__':
    game = SnakesAndLadders()
    num_players = 0
    while not (2 <= num_players <= 4):
        num_players = int(input('Enter the number of players. '
                                'The number must be between 2 and 4: '))
    for i in range(num_players):
        game.add_player(Player(i))
    while not game.winner():
        player = game.current_player()
        print(f"It's {player}'s turn.")
        dice_roll = game.roll_dice()
        print(f"{player} rolled {dice_roll}")
        try:
            game.move_player(dice_roll)
            print(f"{player} moves to {player.position}.")
        except ValueError:
            print(f"{player} cannot move {dice_roll} squares. Wait for the "
                  f"next turn to roll the die again.")
        if dice_roll == 6:
            print(f"{player} get another turn because they rolled 6.")
            dice_roll = game.roll_dice()
            try:
                game.move_player(dice_roll)
                print(f"{player} moves to {player.position}.")
            except ValueError:
                print(f"{player} cannot move {dice_roll} squares. Wait for the "
                      f"next turn to roll the die again.")
        game.end_turn()

    print(f'{game.winner()} won. Congrats!')