#!/usr/bin/env python3

class Day22:
    deck = list(range(0, 10007))

    def dealIntoNewStack(self):
        self.deck = self.deck[::-1]
        
    def cutNCards(self, n):
        self.deck = self.deck[n:] + self.deck[:n]

    def incrementN(self, n):
        deck_copy = [None] * len(self.deck)
        pointer = 0
        while (len(self.deck) > 0):
            deck_copy[pointer] = self.deck.pop(0)
            pointer += n
            if pointer > len(deck_copy):
                pointer = pointer % len(deck_copy)
        self.deck = deck_copy

    def partA(self):
        with open('input.txt') as fp:
            for line in fp:
                words = line.strip().split()
                if words[0] == 'deal':
                    if words[1] == 'with':
                        self.incrementN(int(words[3]))
                    else:
                        self.dealIntoNewStack()
                elif words[0] == 'cut':
                    self.cutNCards(int(words[1]))

if __name__ == '__main__':
    d = Day22()
    d.partA()
    print(d.deck.index(2019))
