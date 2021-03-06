from utils import change_word_ending


class Stats:
    """
    Класс для формирования статистики
    self._name - имя игрока для которого считается статистика
    """

    def __init__(self, player, count_subwords):
        self._name = player
        self._count_subwords = count_subwords

    def __repr__(self):
        count = self._name.quantity_words
        return f'Игра закончилась!\n' \
               f'Вы угадали {count} {change_word_ending("слов", count)} из {self._count_subwords}'

    def save_history(self):
        with open('history/history.txt', 'a+', encoding='utf-8') as outf:
            print(f'У {self._name} отгаданных слов {self._name.quantity_words}', file=outf)
