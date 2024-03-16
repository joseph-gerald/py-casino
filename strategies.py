from game import Session, Games

def martingale_ballsy(session, base_bet, max_bets = -1):
    bet_amount = base_bet
    bets = []

    while len(bets) < max_bets or max_bets == -1:
        try:
            bet = session.play(Games.DICE, bet=bet_amount, win_chance=0.5)
            #print(round(session.balance))

            bets.append(bet)

            if (bet.win):
                bet_amount *= 0.5
            else:
                bet_amount *= 2

        except OverflowError:
            return bets

    return bets

def martingale(session, base_bet, max_bets = -1):
    bet_amount = base_bet
    bets = []

    while len(bets) < max_bets or max_bets == -1:
        try:
            bet = session.play(Games.DICE, bet=bet_amount, win_chance=0.5)
            #print(round(session.balance))

            bets.append(bet)

            if (bet.win):
                bet_amount = base_bet
            else:
                bet_amount *= 2

        except OverflowError:
            return bets

    return bets

# https://www.youtube.com/watch?v=TSU0MSL8tkI
def mattdrenaline(session, base_bet, max_bets = -1):
    bet_amount = base_bet
    bets = []

    while len(bets) < max_bets or max_bets == -1:
        try:
            bet = session.play(Games.DICE, bet=bet_amount, win_chance=0.66)
            #print(round(session.balance))

            bets.append(bet)

            if (bet.win):
                bet_amount = base_bet
            else:
                bet_amount *= 3
        except OverflowError:
            return bets

    return bets

# https://www.youtube.com/watch?v=wThSPaAUEGI
def enjay14cond(session, base_bet, max_bets = -1):
    bet_amount = base_bet
    loss_count = 0
    bets = []

    win_chance = 50
    base_win_chance = win_chance

    while len(bets) < max_bets or max_bets == -1:
        try:
            bet = session.play(Games.DICE, bet=bet_amount, win_chance=win_chance)
            #print(round(session.balance))

            bets.append(bet)

            if (loss_count % 3 == 0):
                win_chance = 0.011
            elif (loss_count % 7 == 0):
                win_chance = 0.009
            elif (loss_count % 9 == 0):
                win_chance = 0.01
            elif (loss_count % 11 == 0):
                win_chance = 0.005
            elif (loss_count % 15 == 0):
                win_chance = 0.009
            elif (loss_count % 18 == 0):
                win_chance = 0.008
            elif (loss_count % 22 == 0):
                win_chance = 0.003

            bet_amount *= 1.03

            if (len(bets) % 12 == 0):
                bet_amount *= 1.07

            if (len(bets) % 3 == 0):
                bet_amount *= 1.11

            if (bet.win):
                bet_amount = base_bet
            else:
                loss_count += 1

            win_chance *= 1.35

            if (win_chance > 0.98): win_chance = 0.98
        except OverflowError:
            return bets

    return bets

def paroli(session, base_bet, max_bets = -1):
    bet_amount = base_bet
    bets = []

    win_streak = 0

    while len(bets) < max_bets or max_bets == -1:
        try:
            bet = session.play(Games.DICE, bet=bet_amount, win_chance=0.5)
            #print(round(session.balance))

            bets.append(bet)

            if (bet.win):
                win_streak += 1
                if (win_streak > 3):
                    bet_amount = base_bet

                bet_amount *= 2
            else:
                bet_amount = base_bet

        except OverflowError:
            return bets

    return bets