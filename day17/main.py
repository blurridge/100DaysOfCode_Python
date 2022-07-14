# Main

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()

for questions in question_data:
    new_q = Question(questions["text"], questions["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("The quiz is complete!")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")