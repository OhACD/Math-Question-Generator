"""
Should generate an arithmetic problem involving multiplication and division
Returns: A prompt and its answer's index.
"""
import random

class MultiplicationQuestion:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.letters = ["A", "B", "C", "D"]
        self.operands = ['*', '/']
        
    def get_multiplication_question(self):
        nums = random.sample(range(self.min, self.max), 2)
        num1, num2 = nums[0], nums[1]        
        operation = random.choice(self.operands)
                
        if operation == '*':
            prompt = f"What is {num1} * {num2}?"
            answer = num1 * num2
        else:
            # No division by zero
            num1 = num1 * num2
            prompt = f"What is {num1} / {num2}?"
            answer = num1 // num2
        
        answers = [
            answer,
            answer + random.randint(1, 5),
            answer - random.randint(1, 5),
            answer + random.randint(6, 10)
        ]
        random.shuffle(answers)
        answer_index = answers.index(answer)
        
        f_answer = [f"{self.letters[i]}) {int(answers[i])}" for i in range(len(answers))]
        
        f_prompt = f"{prompt}\nAnswers:\n" + "\n".join(f_answer)
        
        return f_prompt, answer_index
    