class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0

    def _get_level(self):
        return self._level
    
    def _get_score(self):
        return self._score
    
    def _set_level(self, level):
        if level >= 0:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("lives cannot be negative")

    def _set_score(self, score):
        if score == 1000:
            self._level = score

        else:
            print("the score is getting low")

    level = property(_get_level,_set_level)
    # level = property(_get_level, _set_level)

    def __str__(self):
        return "None: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)