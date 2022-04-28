"""
Игра по составлению слов из букв заданного слова
"""

from random import choice

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
    count_subwords = word_.get_quantity_subwords
    # Приветственное вступление и знакомство с условиями игры
    # функция change_word_ending("слов", count_subwords) склоняет "слово" в зависимости от кол-ва слов
    print(f'Привет, {name_.get_name.title()}!\n'
          f'Составьте {count_subwords} {change_word_ending("слов", count_subwords)} из слова {word_.get_word.upper()}\n'
          'Слова должны быть не короче 3 букв\n'
          'На каждое слово дается 2 попытки'
          'Если хотите получить помощь введите "Help/Помощь"\n'
          'Если хотите завершить игру введите "Стоп/Stop"\n'
          'Чтоб посмотреть отгаданные слова введите "Мои ответы"\n')
    
    # Коллекция для учета подсказанных слов
    used_help_word = list()
    # Общее кол-во попыток
    attempt = count_subwords * 2
    
    # Экземпляр класса Stats
    stat = Stats(name_, count_subwords)

    # Основной цикл, пока есть попытки будем играть
    while attempt:
        
        # Ввод слова пользователем
        answer_subword = input('Введите Ваше слово: \n').lower()

        # Условие на остановку игры по желанию игрока
        if answer_subword in ('stop', 'стоп'):
            break

        # Случай если было введено ключевое слово игры
        if answer_subword in ('помощь', 'help', 'мои ответы'):
            # Если введенное слово помощь или help
            if answer_subword in ('помощь', 'help'):
                # Проверка лимита подсказок
                if len(used_help_word) > 2:
                    print('Вы исчерпали лимит подсказок, подумайте еще раз!\n')
                else:
                    # Цикл, чтоб не подсказывать слова, которые уже были подсказаны
                    while True:
                        # Выбор рандомного слова для подсказки
                        help_word = choice(word_.get_subwords)

                        # Если слова нет в среди уже подсказанных и уже отгаданных слов, то подскажет слово
                        if help_word not in used_help_word and \
                                help_word not in name_.get_used_word:
                            print(f'Попробуйте ввести слово: {help_word}\n')
                            # Добавления подсказанного слова в коллекцию уже подсказанных
                            used_help_word.append(help_word)
                            break
            else:
                # Выдача пользователю на экран угаданных слов
                print(*name_.get_used_word)

        else:
            # Проверка на правильность введенного слова
            if word_.is_correct(answer_subword):
                # Проверка на было ли верное слово введено ранее
                if name_.is_used(answer_subword):
                    print('Это слово уже было\n')
                    continue
                # Добавить в угаданные слова пользователя
                else:
                    name_.add_word(answer_subword)
                    
            # Фидбэк по результатам проверки
            print(f'{word_.get_feedback(answer_subword)}\n')
            
            # Использование попытки
            attempt -= 1
            
    stat.save_history()

    return print(f'\n{stat}')


if __name__ == '__main__':
    word = load_random_word()
    name = Player(input('Введите имя игрока:\n'))

    # Запуск игры
    game_loop(name, word)

    input('Для выхода нажмите Enter')
