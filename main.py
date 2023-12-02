from gameClass import Game


# Главный файл, позволяющий запустить программу

def main() -> None:
    """ Функция создания игры
    :return: Null
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
