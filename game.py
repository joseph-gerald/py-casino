from enum import Enum
import games.dice

class Bet():
    def __init__(self, balance, bet_amount, bet_return, chance, multiplier, data):
        self.bet_amount = bet_amount
        self.bet_return = bet_return

        self.balance = balance
        self.win = bet_return > bet_amount

        self.chance = chance
        self.multiplier = multiplier

        self.data = data

class Games(Enum):
    DICE = games.dice

class Session:
    def __init__(self, balance):
        self.balance = balance

    def play(self, game, **kwargs):
        bet_amount = kwargs.get('bet')
        if (bet_amount > self.balance): raise OverflowError(f"Tried to bet {bet_amount} with a balance of {self.balance}")

        self.balance -= bet_amount

        game_result = game.value.play(**kwargs)

        bet = Bet(self.balance + game_result[1], bet_amount, game_result[0], game_result[1], game_result[2], game_result[3])

        self.balance += bet.bet_return

        return bet