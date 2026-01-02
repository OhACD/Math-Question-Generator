import random
from questions.word import WordQuestion
from questions.arithmetic import ArithmeticQuestion

class QuestionGenerator:
    def main():
        question_type = random.choice(["word", "arithmetic"])
        prompt, answer_index = QuestionGenerator.generate_question(question_type)
        print(prompt)
        print(f"Correct answer is at index: {answer_index}")
        
    
    def generate_question(question_type):
        if question_type == "word":
            return WordQuestion.get_word_question()
        elif question_type == "arithmetic":
            return ArithmeticQuestion.get_arithmetic_question()
        else:
            raise ValueError("Unknown question type")

if __name__ == "__main__":
    QuestionGenerator.main()