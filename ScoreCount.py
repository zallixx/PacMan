class ScoreCounter:

    def __init__(self, score_count=0):
        self.score_count = score_count

    def add(self, x):
        self.score_count += x
        return self.score_count
