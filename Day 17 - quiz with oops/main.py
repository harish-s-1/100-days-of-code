from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz")
print(f"the final score is:{quiz.score}")