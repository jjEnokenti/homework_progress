from random import choice

import requests

from basic_word import BasicWord

PATH = 'https://jsonkeeper.com/b/K8ZH'


def load_random_word(path=PATH):
    """
    Функция принимает и обрабатывает json данные
    выбирает из них случайную коллекцию и формирует экземпляр класса BasicWord
    :param path:
    :return basic:
    """

    # Формирует данные в список словарей из полученной ссылки
    json_data = requests.get(path).json()
    word = choice(json_data)  # Выбор рандомного словаря

    # Создание экземпляра класса BasicWord
    basic = BasicWord(word['word'], word['subwords'])
    return basic


def change_word_ending(word_to_change, num):

    """
    Функция для склонения слов
    :param word_to_change:
    :param num:
    :return changed_word:
    """

    if num % 10 == 0 or num % 10 in tuple(range(5, 10)) or num % 100 in tuple(range(10, 20)):
        return word_to_change
    elif num % 10 in (2, 3, 4):
        changed_word = word_to_change + 'а'
        return changed_word
    elif num % 10 == 1:
        changed_word = word_to_change + 'о'
        return changed_word


def valid_hints(player, word):

    if word.get_hint(player):
        # Цикл, чтоб не подсказывать слова, которые уже были подсказаны
        while True:
            # Выбор рандомного слова для подсказки
            hint = choice(word.get_subwords)

            # Проверка на было ли слово уже подсказано
            if hint not in player.get_hints and hint not in player.get_used_words:
                # Добавления подсказанного слова в коллекцию уже подсказанных
                player.add_hint(hint)
                return f'Попробуйте слово: {hint}'

    return 'Вы исчерпали лимит подсказок, подумайте еще раз!'
