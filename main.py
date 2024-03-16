import matplotlib.pyplot as plt
from game import Session, Games

from strategies import martingale

session = Session(balance=100)
bets = martingale(session, base_bet=10)

# index of bet
x = list(range(1, len(bets) + 1))

# balance history
y = list(map(lambda bet: bet.balance, bets))

#plt.bar(left, balances)

plt.plot(x, y, marker='x', linestyle='-')

plt.grid(True)

plt.xlabel('bet')
plt.ylabel('balance')

plt.title('Balance of Units over bets')

plt.show()