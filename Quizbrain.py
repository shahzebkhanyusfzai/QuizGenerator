

from Questionbank import question_data
class QuestionModel():
    def __init__(self):
        self.questions = [data['text'] for data in question_data]
        self.answers = [data['answer'].lower() for data in question_data]
        self.score = 0
        self.i=0
    def Ask_Question(self):
        while self.i<10:
            self.GivenAns=input(f"Question No {self.i+1}:{self.questions[self.i]}")
            if self.GivenAns.lower()==self.answers[self.i]:
                self.score+=1
                
            self.i+=1
    def DisplayResult(self):
        print(f'You score a total of {self.score}')






