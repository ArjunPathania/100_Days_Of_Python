from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Creating a question bank
question_bank = []
for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

# Initializing the quiz
quiz = QuizBrain(question_bank)

# Running the quiz
while quiz.still_has_questions():
    quiz.next_question()

# End of quiz
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
