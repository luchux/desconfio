import random

class Player():


    def __init__(self, name):
        self.name = name
        self.hand = []
        self.GAME_NAIVE = [1]

    def ask_game(self):
        #naive: retrieve the first  card
        cards = [self.hand[0]]
        self.hand = self.hand[1:]
        return cards

    def ask_choice(self):
        #TODO: remove constant that defines a naive game of cards.
        pos = random.randint(0, len(self.hand)-1)
        print 'pos: {0}'.format(pos)
        return [self.hand[pos]]

    def receive_cards(self, hand):
        self.hand = hand

    def ask_unbelieve(self):
        a = [True, False]
        random.shuffle(a)
        return a[0]

    def won(self):
        return self.hand == []

class Deck():

    def reveal_last_game(self):
        return self.last_game

    def get_hand(self):
        return self.hand


class Judge():

    def __init__(self):
        self.last_game = None
        self.hand = []
        self.count = 0

    def play(self,player, oponent):

        print 'turno de: {0}'.format(player.name)

        choice  = player.ask_choice()
        print '{0} dice: {1}'.format(player.name,choice)

        cards = player.ask_game()
        print 'elije: {0}'.format(cards)

        self.hand.extend(cards)
        print 'MESA: {0}'.format(self.hand)

        self.last_game = cards



        unbelieve = oponent.ask_unbelieve()

        if unbelieve:
            print '{0} desconfia'.format(oponent.name)
            #Unbelieve, are they different?
            print 'last: {0}'.format(self.last_game)
            if self.last_game != choice:

                print 'se descubre la mentira'
                #Unbelieving was right, oponent win hand
                player.hand.extend(self.hand)
                self.hand = []
                print '{0}:{1}'.format(player.name, player.hand)
                print '{0}:{1}'.format(oponent.name,oponent.hand)
                print

                if oponent.won():
                    return oponent
                else:
                    return self.play(oponent,player)
            else:
                #Unbelieving was wrong, player win hand
                'se equivoca el desconfio'
                oponent.hand.extend(self.hand)
                self.hand = []
                print '{0}:{1}'.format(player.name, player.hand)
                print '{0}:{1}'.format(oponent.name,oponent.hand)
                print
                if player.won():
                    return player
                else:
                    return self.play(player,oponent)

            #In every case, once unbelieved one of both take the whole stack.
            self.hand = []

        else:
            print '{0}:{1}'.format(player.name, player.hand)
            print '{0}:{1}'.format(oponent.name, oponent.hand)
            if player.won():
                return player
            return self.play(oponent, player)

class Game():

    def __init__(self):

        self.player1 = Player('juan')
        self.player2 = Player('ramiro')
        self.judge = Judge()

    def give_cards(self):

        cards1, cards2 = self.hand.split_random()
        self.player1.receive_cards(cards1)
        self.player2.receive_cards(cards2)

    def start_game(self):

        winer = self.judge.play(self.player1, self.player2)
        print 'winner: {0}'.format(winer.name)
