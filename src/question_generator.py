import random
from questions.word import WordQuestion
from questions.arithmetic import ArithmeticQuestion
from questions.counting import CountingQuestion
from questions.multiplication import MultiplicationQuestion

class QuestionGenerator:
    
    def __init__(self):
        self.word_question = WordQuestion(["Alice", "Bob", "Charlie", "Diana"], 2, 6)
        self.arithmetic_question = ArithmeticQuestion(2, 12)
        self.counting_question = CountingQuestion()
        self.multiplication_question = MultiplicationQuestion(2, 8)
    
    def main(self):
        question_type = random.choice(["word", "arithmetic", "counting", "multiplication"])
        prompt, answer_index = self.generate_question(question_type)
        print(prompt)
        print(f"Correct answer is at index: {answer_index}")
        
    
    def generate_question(self, question_type):
        if question_type == "word":
            return self.word_question.get_word_question()
        elif question_type == "arithmetic":
            return self.arithmetic_question.get_arithmetic_question()
        elif question_type == "counting":
            return self.counting_question.get_counting_question()
        elif question_type == "multiplication":
            return self.multiplication_question.get_multiplication_question()
        else:
            raise ValueError("Unknown question type")

if __name__ == "__main__":
    generator = QuestionGenerator()
    generator.main()