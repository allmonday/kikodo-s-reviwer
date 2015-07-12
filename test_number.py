#coding:utf-8
import codecs
import random
from base import BaseTester

class NiHong(BaseTester):

    def __init__(self):
        super(NiHong, self).__init__()
        self.question_number = 31

    def init_choose(self):
        print "test numbers from 1- 100"

    def prepare_test_material(self):
        all_question = []
        with codecs.open('./resources/number.test', 'r', encoding="utf-8") as q:
            lines = q.readlines()
            for line in lines:
                question, answer = line.strip().split(':')
                answer = answer.split(',')
                all_question.append((question, answer))

        self.questions = random.sample(all_question, self.question_number)

if __name__ == "__main__":

    n = NiHong()
    n()
