#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value if (type(value) is (str)) else print('The value must be a string.')
    def is_sentence(self):
        return True if str(self.value).endswith('.') else False
    def is_question(self):
        return True if str(self.value).endswith('?') else False
    def is_exclamation(self):
        return True if str(self.value).endswith('!') else False
    def count_sentences(self):
        sentence_count = 0
        sentence_count += self.value.count('.')
        sentence_count += self.value.count('?')
        sentence_count += self.value.count('!')
        return sentence_count