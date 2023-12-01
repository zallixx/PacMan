import pyray


class Audio:
    sounds = []

    def __init__(self, game, volume: int, musicname='sounds/begin_sound.wav'):
        """Класс звука
        :param game: все переменные игры
        :type game: Game
        :param volume: громкость
        :type volume: int
        :param musicname: путь до звука
        :type musicname: str
        """
        self.game = game
        self.volume = volume/100
        self.track = pyray.load_sound(musicname)
        self.sounds.append(self)

    def play_track(self):
        """Проиграть звук
        :return: Null
        """
        pyray.set_sound_volume(self.track, self.volume)
        pyray.play_sound(self.track)

    @staticmethod
    def update_volume(volume):
        """Обновить громкость у всех звуков
        :param volume: громкость
        :type volume: int
        :return: Null
        """
        for i in Audio.sounds:
            i.volume = volume
