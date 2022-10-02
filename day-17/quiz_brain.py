# ask qesutions
# check if the answer is correct
# check if reach end og quiz

class QuizBrain:
    def __init__(self, q):
        self.question_number = 0
        self.question_list = q
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number].text
        user_answer = input(f"Q.{self.question_number+1}: {question} (True/False)?: ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, actual_ans):
        if user_ans.strip().lower() == actual_ans.strip().lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct a answer was: {actual_ans}")
        print(f"Your score is {self.score}/{self.question_number+1}")
        print("\n")
