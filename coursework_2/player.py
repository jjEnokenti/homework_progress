class Player:
    """
    Класс Игрока

    Поля:
    self._name - Имя игрока
    self._used_words - использованные слова

    Методы:
    quantity_words(self) - геттер, возвращает кол-во использованных слов
    add_word(self, new_word) - добавляет слово в список использованных слов если слово верное
    is_used(self, new_word) - проверяет слово было ли использованно ранее
    get_name(self) - геттер, возвращает имя игрока
    get_used_word(self) - геттер, возвращает список уже использованных слов
    """

    def __init__(self, name):
        self._name = name
        self._used_words = list()


    def __repr__(self):
        return self._name

    @property
    def quantity_words(self):
        return len(self._used_words)

    def add_word(self, new_word):
        self._used_words.append(new_word)

    def is_used(self, new_word):
        return new_word in self._used_words

    @property
    def get_name(self):
        return self._name

    @property
    def get_used_word(self):
        return self._used_words
