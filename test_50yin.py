#coding:utf-8
import random
from base import BaseTester

class NiHong(BaseTester):

    def __init__(self):
        super(NiHong, self).__init__()
        self.question_number = 30

    def init_choose(self):
        choose = raw_input("choose: [1] default: test hiragana for katakana, [2]: test katakana for hiragana: ")

        if choose not in ['1', '2', '１', '２', '']:
            print "invalid input, exit"
            exit()

        if choose in ('1', '１', ''):
            print "switch to hiragana, please"
            self.choose = 'hiragana'

        elif choose in ('2', '２'):
            print "switch to katakana, please"
            self.choose = 'katakana'

    def prepare_test_material(self):
        hiragana = u'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやいゆえよらりるれろわいうえをん'
        katakana = u'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤイユエヨラリルレロワイウエヲン'

        if self.choose == "hiragana":
            group = zip(katakana, hiragana)
            self.mapping = dict(zip(hiragana, katakana))

        elif self.choose == "katakana":
            group = zip(hiragana, katakana)
            self.mapping = dict(zip(katakana, hiragana))

        self.questions = random.sample(group, self.question_number)

if __name__ == "__main__":

    n = NiHong()
    n()
