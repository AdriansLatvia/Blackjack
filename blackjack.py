import random
import time


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} no {self.suit}"

    def value(self):
        if self.rank in ["Jack", "Queen", "King"]:
            return 10
        if self.rank == "Ace":
            return 11
        return int(self.rank)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        self.cards = [Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.aces = 0

    def add(self, card):
        self.cards.append(card)
        self.total += card.value()
        if card.rank == "Ace":
            self.aces += 1
        while self.total > 21 and self.aces:
            self.total -= 10
            self.aces -= 1


class Blackjack:
    def __init__(self):
        self.chips = 1000

    def play_round(self):
        deck = Deck()
        player = Hand()
        dealer = Hand()

        print(f"\nŽetoni: ${self.chips}")
        bet = int(input("Likme: $"))

        for _ in range(2):
            player.add(deck.deal())
            dealer.add(deck.deal())

        while True:
            print("\nDīleris:")
            print("[Slēpta kārts]")
            print(dealer.cards[1])

            print("\nSpēlētājs:")
            for c in player.cards:
                print(c)
            print("Kopā:", player.total)

            if player.total > 21:
                print("Pārkāpts 21!")
                self.chips -= bet
                return

            choice = input("H - ņemt, S - stāvēt: ").upper()
            if choice == "H":
                player.add(deck.deal())
            else:
                break

        print("\nDīleris:")
        for c in dealer.cards:
            print(c)
        print("Kopā:", dealer.total)

        while dealer.total < 17:
            time.sleep(1)
            dealer.add(deck.deal())
            print("Dīleris ņem:", dealer.cards[-1])
            print("Kopā:", dealer.total)

        if dealer.total > 21 or player.total > dealer.total:
            print("Tu uzvarēji!")
            self.chips += bet
        elif player.total < dealer.total:
            print("Dīleris uzvarēja.")
            self.chips -= bet
        else:
            print("Neizšķirts.")

    def start(self):
        print("Blackjack 21")
        while self.chips > 0:
            self.play_round()
            again = input("Spēlēt vēl? (Y/N): ").upper()
            if again != "Y":
                break
        print("Spēle beigusies. Žetoni:", self.chips)


if __name__ == "__main__":
    Blackjack().start()  # Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run itimport random
import time


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} no {self.suit}"

    def value(self):
        if self.rank in ["Jack", "Queen", "King"]:
            return 10
        if self.rank == "Ace":
            return 11
        return int(self.rank)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        self.cards = [Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.aces = 0

    def add(self, card):
        self.cards.append(card)
        self.total += card.value()
        if card.rank == "Ace":
            self.aces += 1
        while self.total > 21 and self.aces:
            self.total -= 10
            self.aces -= 1


class Blackjack:
    def __init__(self):
        self.chips = 1000

    def play_round(self):
        deck = Deck()
        player = Hand()
        dealer = Hand()

        print(f"\nŽetoni: ${self.chips}")
        bet = int(input("Likme: $"))

        for _ in range(2):
            player.add(deck.deal())
            dealer.add(deck.deal())

        while True:
            print("\nDīleris:")
            print("[Slēpta kārts]")
            print(dealer.cards[1])

            print("\nSpēlētājs:")
            for c in player.cards:
                print(c)
            print("Kopā:", player.total)

            if player.total > 21:
                print("Pārkāpts 21!")
                self.chips -= bet
                return

            choice = input("H - ņemt, S - stāvēt: ").upper()
            if choice == "H":
                player.add(deck.deal())
            else:
                break

        print("\nDīleris:")
        for c in dealer.cards:
            print(c)
        print("Kopā:", dealer.total)

        while dealer.total < 17:
            time.sleep(1)
            dealer.add(deck.deal())
            print("Dīleris ņem:", dealer.cards[-1])
            print("Kopā:", dealer.total)

        if dealer.total > 21 or player.total > dealer.total:
            print("Tu uzvarēji!")
            self.chips += bet
        elif player.total < dealer.total:
            print("Dīleris uzvarēja.")
            self.chips -= bet
        else:
            print("Neizšķirts.")

    def start(self):
        print("Blackjack 21")
        while self.chips > 0:
            self.play_round()
            again = input("Spēlēt vēl? (Y/N): ").upper()
            if again != "Y":
                break
        print("Spēle beigusies. Žetoni:", self.chips)


if __name__ == "__main__":
    Blackjack().start()
