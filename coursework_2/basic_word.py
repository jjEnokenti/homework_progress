class BasicWord:
    """
    Описание класса слов с подсловами

    Поля:
    self._word - Слово для которого отгадываются подслова
    self._subwords - коллекция подслов слова word

    Методы:
    is_correct(self, subword) - принимает подслова от
    игрока и проверяет его корректность
    get_quantity_subwords(self) - геттер, возвращает количество существующих подслов
    get_subwords(self) - геттер, возвращает коллекцию подслов
    get_word(self) - геттер, возвращает основное слово
    get_feedback(self, subword) - возвращает фидбек правильно не правильно
    """

    def __init__(self, word, subwords):
        self._word = word
        self._subwords = subwords

    def __repr__(self):
        return self._word

    def is_correct(self, subword):
        return subword.lower() in self._subwords

    @property
    def get_quantity_subwords(self):
        return len(self._subwords)

    @property
    def get_subwords(self):
        return self._subwords

    @property
    def get_word(self):
        return self._word

    def get_feedback(self, subword):
        if self.is_correct(subword):
            return 'Верно, молодец!'
        return 'Неверно, подумай еще!'
