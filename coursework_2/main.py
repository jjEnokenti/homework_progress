"""
Игра по составлению слов из букв заданного слова
"""

from utils import load_random_word, change_word_ending
from player import Player
from stats import Stats


def game_loop(name_, word_):
    """
    Основной цикл запуска игры
    :param name_:
    :param word_:
    :return stat: возвращает статистику
    """

    # Кол-во подслов в слове
    count_subwords = word_.count_subwords
    # Общее кол-во попыток
    attempt = count_subwords * 2
    
    # Приветственное вступление и знакомство с условиями игры
    # функция change_word_ending("слов", count_subwords) склоняет "слово" в зависимости от кол-ва слов
    print(f'Привет, {name_.get_name.title()}!',
          f'Составьте {count_subwords} {change_word_ending("слов", count_subwords)} из слова {word_.get_word.upper()}',
          f'Слова должны быть не короче {len(word_.minimal_word())} букв',
          'На каждое слово дается 2 попытки',
          'Если хотите получить помощь введите "Help/Помощь"',
          'Если хотите завершить игру введите "Стоп/Stop"',
          'Чтоб посмотреть отгаданные слова введите "Мои ответы"'
          'Поехали, Ваше первое слово?', sep='\n')

    # Экземпляр класса Stats
    stat = Stats(name_, count_subwords)

    # Основной цикл, пока есть попытки будем играть
    while attempt:

        # Ввод слова пользователем
        answer = input('Введите Ваше слово: \n').lower()

        # Условие на остановку игры по желанию игрока
        if answer in ('stop', 'стоп'):
            break

        # Случай если было введено ключевое слово игры
        if answer in ('помощь', 'help', 'мои ответы'):
            # Если введенное слово помощь или help
            if answer in ('помощь', 'help'):
                # Проверка лимита подсказок
                if name_.count_hints() > 2:
                    print('Вы исчерпали лимит подсказок, подумайте еще раз!\n')
                else:
                    # Цикл, чтоб не подсказывать слова, которые уже были подсказаны
                    while True:
                        # Выбор рандомного слова для подсказки
                        hint = word_.get_hint()

                        # Если слова нет в среди уже подсказанных и уже отгаданных слов, то подскажет слово
                        if hint not in zip(name_.get_hints, name_.get_used_words):
                            print(f'Попробуйте слово: {hint}\n')
                            # Добавления подсказанного слова в коллекцию уже подсказанных
                            name_.add_hint(hint)
                            break
            else:
                # Выдача пользователю на экран угаданных слов
                print(*name_.get_used_word)

        else:
            # Проверка на правильность введенного слова
            if word_.is_correct(answer):
                # Проверка на было ли верное слово введено ранее
                if name_.is_used(answer):
                    print('Это слово уже было\n')
                    continue
                # Добавить в угаданные слова пользователя
                else:
                    name_.add_word(answer)

            # Фидбэк по результатам проверки
            print(f'{word_.get_feedback(answer)}\n')

            attempt -= 1
            # Завершение игры по окончанию попыток либо победе
            if not attempt or name_.count_words() == count_subwords:
                break

    stat.save_history()

    return print(f'\n{stat}')


if __name__ == '__main__':
    word = load_random_word()
    name = Player(input('Введите имя игрока:\n'))

    # Запуск игры
    game_loop(name, word)

    input('Для выхода нажмите Enter')
