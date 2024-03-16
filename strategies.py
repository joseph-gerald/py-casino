from game import Session, Games

def martingale(session, base_bet):
    bet_amount = base_bet
    bets = []

    while True:
        try:
            bet = session.play(Games.DICE, bet=bet_amount, win_chance=0.5)
            #print(round(session.balance))

            bets.append(bet)
        except OverflowError:
            break

    return bets