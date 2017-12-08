""" This class encapsulte the 'Elo' class, which is use for elo computing"""

class Elo(object):
    """class that handles elo computing"""

    def winProbability(self, eloDiff):
        """compute the winning probability depending on the rating advantage"""
        return round(1/(10**((-eloDiff/400.0))+1),2)

    def compute(self, elo1, elo2, result):
        """compute the new elo after the result for the player whose elo is elo1 pov"""
        return elo1 + 10*(result -self.winProbability(elo1-elo2))
