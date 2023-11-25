import pyray


class Audio:
    def __init__(self, game, volume, musicname='sounds/begin_sound.wav'):
        self.game = game
        self.volume = volume
        self.track = pyray.load_sound(musicname)

    def play_track(self):
        pyray.set_sound_volume(self.track, self.volume)
        pyray.play_sound(self.track)


