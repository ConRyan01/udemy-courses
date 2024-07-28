from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item['question']
    question_answer = item['correct_answer']
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print(f"You've completed the quiz!\nYou're final score was: {quiz.score}/{quiz.question_number}")