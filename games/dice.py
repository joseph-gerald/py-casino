import random

def play(bet, win_chance):
    MULTIPLIER = 1 / win_chance * 0.99

    ROLL = random.random()

    RETURNS = bet * MULTIPLIER if ROLL < win_chance else 0

    return (RETURNS, win_chance, MULTIPLIER, {
        "ROLL": ROLL
    })

if __name__ == "__main__":
    print(play(20, 0.2))