#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class BaseTester(object):

    def __init__(self):
        self.questions = [] # [(question, answer),]
        self.errors = [] # [(question, answer, your_answer),]

        self.score = 0
        self.choose = ""
        self.mapping = {} # find your answer's question

        self.question_number = 30

    def init_choose(self):
        """
        override me
        """
        pass

    def prepare_test_material(self):
        """
        override me
        """
        pass

    def record_errors(self, question, default_answer, your_answer):
        self.errors.append((question, default_answer, your_answer))

    def runner(self):

        for question, default_answer in self.questions:
            your_answer = raw_input(u"\nanswer for {}: ".format(question))


            if your_answer == default_answer or your_answer in default_answer:  # to check answer array
                self.score += 1
                print(' correct'),

            else:
                if type(default_answer) is list:
                    default_answer = " or ".join(default_answer)
                print(' oops, answer is: {}, your answer is for {}'.format(
                    default_answer, self.mapping.get(unicode(your_answer), "not found"))),

                self.record_errors(question, default_answer, your_answer)

    def report(self):

        print "your score: {:0.2f}".format(self.score/float(self.question_number)),
        if self.score == self.question_number:
            print "congratulation !!!!"
        else:
            print "errors"
            for question, default_answer, your_answer in self.errors:
                print "{}: {}, your answer: {}".format(question, default_answer, your_answer)

    def __call__(self):
        """
        execute test
        """
        self.init_choose()
        self.prepare_test_material()
        self.runner()
        self.report()
