class LifeCounter:

    def __init__(self, life_count=3):
        self.life_count = life_count

    def add(self):
        self.life_count += 1
        return self.life_count

    def remove(self):
        self.life_count -= 1
        if self.life_count < 0:
            return 1 / 0
        return self.life_count
