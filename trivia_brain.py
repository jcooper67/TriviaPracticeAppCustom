from question_class import Question

class Trivia_Brain:
    def __init__(self):
        self.question_bank =[]
        self.score = 0
        self.question_number = 0
        self.categories = ["General Knowledge", "Animals","Arts", "Politics", "History"]

    def create_questions(self,question_data):
        for question in question_data:
            question_text = question['question']
            question_answer = question['correct_answer']
            question_text = self.fix_question_text(question_text)
            new_question = Question(question_text,question_answer)
            self.question_bank.append(new_question)

    def fix_question_text(self,question_text):
        question_text = question_text.replace("&#039;","'")
        question_text = question_text.replace("&quot;",'"')
        return question_text



    def check_answer(self, user_answer):
        correct_answer = self.question_bank[self.question_number].answer
        self.question_number+=1
        if user_answer == correct_answer:

            return True

        else:

            return False


    def next_question(self):
        if self.question_number <= len(self.question_bank)-1:
            question = self.question_bank[self.question_number].question
            return question
        else :
            return False