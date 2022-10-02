from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for ele in question_data:
    question_bank.append( Question(ele["text"], ele["answer"]) )

quizBrain = QuizBrain(question_bank)

while quizBrain.still_has_question():
    quizBrain.next_question()

print("You've complete the quiz.")
print(f"Your final score was: {quizBrain.score}/{len(question_bank)}.")

