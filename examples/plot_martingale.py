import matplotlib.pyplot as plt
from game import Session, Games

from strategies import martingale_ballsy, martingale, mattdrenaline, enjay14cond

max_bets = 100
sessions = [0]*100

for i in range(50):
    session = Session(balance=100)
    bets = martingale(session, base_bet=10, max_bets=max_bets)
    
    for i2 in range(len(bets) - 1):
        sessions[i2] += 1

    # index of bet
    x = list(range(1, len(bets) + 1))

    # balance history
    y = list(map(lambda bet: bet.balance, bets))

    plt.scatter(x, y, color="red", alpha=0.05)

plt.plot(range(len(sessions)), sessions, color="red")

plt.grid(True)

plt.xlabel('bet')
plt.ylabel('balance')
plt.legend(loc="upper left")

plt.title('Balance of Units over bets')

plt.show()