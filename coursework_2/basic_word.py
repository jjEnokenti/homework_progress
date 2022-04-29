class BasicWord:
    """
    Описание класса слов с подсловами

    Поля:
    self.__word - Слово для которого отгадываются подслова
    self.__subwords - коллекция подслов слова word

    Методы:
    is_correct(self, subword) - принимает подслова от
    игрока и проверяет его корректность
    get_quantity_subwords(self) - геттер, возвращает количество существующих подслов
    get_subwords(self) - геттер, возвращает коллекцию подслов
    get_word(self) - геттер, возвращает основное слово
    get_feedback(self, subword) - возвращает фидбек правильно не правильно
    minimal_word(self) - Возвращает самое короткое слово
    give_hint(self) - дает подсказку
    """

    def __init__(self, word, subwords):
        self.__word = word
        self.__subwords = list(set(subwords))

    def __repr__(self):
        return self.__word

    def is_correct(self, subword):
        return subword.lower() in self.__subwords

    @property
    def count_subwords(self):
        return len(self.__subwords)

    @property
    def get_subwords(self):
        return self.__subwords

    @property
    def get_word(self):
        return self.__word

    def get_hint(self, name):
        if name.count_hints() < 3:
            return True
        return False

    def get_feedback(self, subword):
        if self.is_correct(subword):
            return 'Верно, молодец!'
        return 'Неверно, подумай еще!'

    def minimal_word(self):
        return min(self.__subwords, key=len)
