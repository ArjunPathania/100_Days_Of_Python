from question_model import Question
from data import QuestionBank
from quiz_brain import QuizBrain
from ui import QuizInterface


#
# Initialize the QuestionBank to retrieve question data
question_bank_instance = QuestionBank()
question_data = question_bank_instance.question_data  # Retrieve questions data from the API
#
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# print(len(question_bank))
#Initialize UI
quiz_ui = QuizInterface(quiz)

