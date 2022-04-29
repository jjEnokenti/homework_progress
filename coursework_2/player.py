class Player:
    """
    Класс Игрока

    Поля:
    self.__name - Имя игрока
    self.__used_words - использованные слова

    Методы:
    quantity_words(self) - геттер, возвращает кол-во использованных слов
    add_word(self, new_word) - добавляет слово в список использованных слов если слово верное
    is_used(self, new_word) - проверяет слово было ли использованно ранее
    get_name(self) - геттер, возвращает имя игрока
    get_used_word(self) - геттер, возвращает список уже использованных слов
    get_hints(self) - Возвращает подсказанные слова
    count_hints(self) - возвращает кол-во подсказанных слов
    add_hint(self, hint) - добавляет подсказанное слово в подсказанные
    """

    def __init__(self, name):
        self.__name = name
        self.__used_words = list()
        self.__hint_words = list()

    def __repr__(self):
        return self.__name

    def add_word(self, new_word):
        self.__used_words.append(new_word)

    def add_hint(self, hint):
        self.__hint_words.append(hint)

    @property
    def quantity_words(self):
        return len(self.__used_words)

    @property
    def get_name(self):
        return self.__name

    @property
    def get_used_words(self):
        return self.__used_words

    @property
    def get_hints(self):
        return self.__hint_words

    def is_used(self, new_word):
        return new_word in self.__used_words

    def count_hints(self):
        return len(self.__hint_words)

    def count_words(self):
        return len(self.__used_words)
