from juego import Judge, Player, Game
import random

if __name__ == '__main__':
    shuffle = [1,1,1,1,2,2,2,2,3,3,3,3]
    random.shuffle(shuffle)
    hand1, hand2 = shuffle[:len(shuffle)/2], shuffle[len(shuffle)/2:]

    p = Player('juan')
    p2 = Player('jorge')
    p.receive_cards(hand1)
    p2.receive_cards(hand2)

    j = Judge()

    print '{0}:  {1}'.format(p.name,p.hand)
    print '{0}: {1}'.format(p2.name,p2.hand)

    print 'comienza el juego'

    winer = j.play(p,p2)
    print 'WON: {0}'.format(winer.name)



