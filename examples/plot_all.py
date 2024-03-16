import matplotlib.pyplot as plt
from game import Session, Games

from strategies import martingale_ballsy, martingale, mattdrenaline, enjay14cond

max_bets = 200

for i in range(50):
    for colour, strategy in [["blue", mattdrenaline, ], ["lightblue", martingale_ballsy], ["green", martingale], ["red", enjay14cond]]:
        session = Session(balance=100)
        bets = strategy(session, base_bet=25, max_bets=max_bets)
        
        # index of bet
        x = list(range(1, len(bets) + 1))

        # balance history
        y = list(map(lambda bet: bet.balance, bets))

        plt.plot(x, y, color=colour, label=strategy.__name__ if i == 1 else None)

plt.grid(True)

plt.xlabel('bet')
plt.ylabel('balance')
plt.legend(loc="upper left")

plt.title('Balance of Units over bets')

plt.show()