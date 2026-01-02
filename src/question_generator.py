import random
from questions.word import WordQuestion
from questions.arithmetic import ArithmeticQuestion
from questions.counting import CountingQuestion
from questions.multiplication import MultiplicationQuestion

class QuestionGenerator:
    word_question = WordQuestion(["Alice", "Bob", "Charlie", "Diana"], 2, 10)
    arithmetic_question = ArithmeticQuestion(2, 16)
    counting_question = CountingQuestion()
    multiplication_question = MultiplicationQuestion(2, 12)
    
    def main():
        question_type = random.choice(["word", "arithmetic", "counting", "multiplication"])
        prompt, answer_index = QuestionGenerator.generate_question(question_type)
        print(prompt)
        print(f"Correct answer is at index: {answer_index}")
        
    
    def generate_question(question_type):
        if question_type == "word":
            return QuestionGenerator.word_question.get_word_question()
        elif question_type == "arithmetic":
            return QuestionGenerator.arithmetic_question.get_arithmetic_question()
        elif question_type == "counting":
            return QuestionGenerator.counting_question.get_counting_question()
        elif question_type == "multiplication":
            return QuestionGenerator.multiplication_question.get_multiplication_question()
        else:
            raise ValueError("Unknown question type")

if __name__ == "__main__":
    QuestionGenerator.main()