import pyray


class Audio:
    def __init__(self, game, musicname='sounds/begin_sound.wav'):
        self.game = game
        self.track = pyray.load_sound(musicname)

    def play_track(self):
        pyray.play_sound(self.track)


