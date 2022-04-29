from utils import load_random_word, change_word_ending, valid_hints
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
    # Экземпляр класса Stats
    stat = Stats(name_, count_subwords)
    # Общее кол-во попыток
    attempt = count_subwords * 2 + 1

    key_words = {
        'помощь': None,
        'help': None,
        'мои ответы': name_.get_used_words
    }

    # Приветственное вступление и знакомство с условиями игры
    # функция change_word_ending("слов", count_subwords) склоняет "слово" в зависимости от кол-ва слов
    print(f'Привет, {name_.get_name.title()}!',
          f'Составьте {count_subwords} {change_word_ending("слов", count_subwords)} из слова {word_.get_word.upper()}',
          f'Слова должны быть не короче {len(word_.minimal_word())} букв',
          'На каждое слово дается 2 попытки',
          'Если хотите получить помощь введите "Help/Помощь"',
          'Чтоб посмотреть отгаданные слова введите "Мои ответы"',
          'Если хотите завершить игру введите "Стоп/Stop"',
          'Поехали, Ваше первое слово?', sep='\n')

    # Основной цикл
    while True:

        # Ввод слова пользователем
        answer = input('\nВведите Ваше слово: \n').lower()

        attempt -= 1
        # Завершение игры по окончанию попыток, по желанию либо по окончанию слов
        if not attempt or name_.count_words() == count_subwords or answer in ('stop', 'стоп'):
            break

        # Случай если было введено ключевое слово подсказок по игре
        if answer in key_words:
            # Выдача пользователю угаданных им слов
            if answer == 'мои ответы':
                print(*key_words[answer])
            # Если введенное слово помощь или help
            else:
                # Показать подсказку или исчерпан лимит
                print(valid_hints(name_, word_))

        else:
            # Проверка на правильность введенного слова
            if word_.is_correct(answer):
                # Проверка было ли верное слово введено ранее
                if name_.is_used(answer):
                    print('Это слово уже было\n')
                    continue

                # Добавить в угаданные слова пользователя
                name_.add_word(answer)

            # Фидбэк по результатам проверки
            print(f'{word_.get_feedback(answer)}')

    # Запись статистики в файл history.txt
    stat.save_history()

    return stat


if __name__ == '__main__':
    word = load_random_word()
    name = Player(input('Введите имя игрока:\n'))

    # Запуск игры
    print(game_loop(name, word))

    input('Для выхода нажмите Enter')
