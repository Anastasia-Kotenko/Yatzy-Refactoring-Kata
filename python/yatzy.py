from collections import Counter

MAX = 7
MIN = 1


class Yatzy:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        total = 0
        total = d1 + d2 + d3 + d4 + d5
        return total

    @staticmethod
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        sum = 0
        d = [d1, d2, d3, d4, d5]
        for i in d:
            if i == 1:
                sum += 1
        return sum

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        sum = 0
        for d in [d1, d2, d3, d4, d5]:
            if d == 2:
                sum += 2
        return sum

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        s = 0
        for d in [d1, d2, d3, d4, d5]:
            if d == 3:
                s += 3
        return s

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4):
                sum += 4
        return sum

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if (self.dice[i] == 5):
                s = s + 5
        return s

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)):
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum

    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        counts = Counter([d1, d2, d3, d4, d5])
        for val in reversed(range(MIN, MAX)):
            if counts[val] == 2:
                return val * 2
        return 0

    @staticmethod
    def two_pair(d1, d2, d3, d4, d5):
        counts = Counter([d1, d2, d3, d4, d5])
        pair = [val for val, count in counts.items() if count >= 2]
        if len(pair) == 2:
            return sum(pair) * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(d1, d2, d3, d4, d5):
        tallies = Counter([d1, d2, d3, d4, d5])
        for val, count in tallies.items():
            if count >= 4:
                return val * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = Counter([d1, d2, d3, d4, d5])
        for val, count in t.items():
            if count >= 3:
                return val * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        if 2 in tallies and 3 in tallies:
            return (tallies.index(2) + 1) * 2 + (tallies.index(3) + 1) * 3
        else:
            return 0