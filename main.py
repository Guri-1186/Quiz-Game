from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_brain import PrintFinalInfo

question_bank = [Question(item["question"], item["correct_answer"]) for item in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

final_info = PrintFinalInfo(quiz)
final_info.display()

