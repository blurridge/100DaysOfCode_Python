# Quiz Brain

class QuizBrain:

    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        curr_q = self.question_list[self.question_number]
        self.question_number+=1
        user_ans = input(f"Q.{self.question_number} {curr_q.text} (true/false): ").lower()
        self.check_answer(user_ans, curr_q.answer)

    def check_answer(self, user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            print("Correct answer!")
            self.score += 1
        else:
            print(f"Wrong answer. Correct answer is {corr_ans}.")
        print(f"Your current score is: {self.score}/{len(self.question_list)}\n")