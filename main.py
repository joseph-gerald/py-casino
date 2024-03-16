import matplotlib.pyplot as plt
from game import Session, Games
from statistics import mean

from strategies import martingale_ballsy, martingale, mattdrenaline, enjay14cond, paroli

sessions_to_simulate = 1000

max_bets = 100
base_bet = 1
initial_balance = 4430

sessions = [0]*(max_bets-1)
sessions_balance = [0]*(max_bets-1)
sessions_left = 0
sessions_plus = 0

for i in range(sessions_to_simulate):
    session = Session(balance=initial_balance)
    bets = martingale(session, base_bet=base_bet, max_bets=max_bets)
    
    for i2 in range(len(bets) - 1):
        sessions[i2] += 1*(initial_balance/sessions_to_simulate)
        sessions_balance[i2] += bets[i2].balance

    # index of bet
    x = list(range(1, len(bets) + 1))

    # balance history
    y = list(map(lambda bet: bet.balance, bets))

    if (len(bets) == max_bets):
        sessions_left += 1

    if (session.balance > initial_balance and len(bets) == max_bets):
        sessions_plus += 1
    #print(session.balance)

for i2 in range(len(sessions_balance)):
    sessions_balance[i2] /= sessions[i2]*(sessions_to_simulate/initial_balance) #sessions_to_simulate

plt.plot(range(len(sessions)), sessions, label="Sessions Betting", color="red")
plt.plot(range(len(sessions_balance)), sessions_balance, label="Average Session Balance", color="green")

plt.grid(True)

plt.xlabel('bets')
plt.ylabel('balance')
plt.legend(loc="upper left")

plt.title(f"Balance of Units over Bets | +{sessions_plus}/{sessions_to_simulate} | ~{sessions_left}/{sessions_to_simulate}")

sessions_balance.sort()

print()
print("STATISTICS")
print("HIT %", sessions_plus/sessions_to_simulate*100, sessions_plus, sessions_to_simulate)
print("LIV %", sessions_left/sessions_to_simulate*100, sessions_left, sessions_to_simulate)
print("AVERAGE BALANCE", mean(sessions_balance))
try:
    print("TOP 5%", mean(sessions_balance[:-round(len(sessions_balance)*0.05)]))
except:
    pass
print("WIN BALANCE", sessions_balance[-1])
print()

plt.show()