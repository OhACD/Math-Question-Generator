"""
Should generate an arithmetic problem involving addition and subtraction.
Returns: A prompt and its answer's index.
"""
import random

class ArithmeticQuestion:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.letters = ["A", "B", "C", "D"]
        self.operands = ['+', '-']
        
    def get_arithmetic_question(self):
        nums = random.sample(range(self.min, self.max), 3)
        num1, num2, num3 = nums[0], nums[1], nums[2]        
        operands = random.choices(self.operands, k=2)
        sign1, sign2 = operands[0], operands[1]
        
        prompts = [
            f"What is {num1} {sign1} {num2} {sign2} {num3}?",
            f"What is {num3} {sign2} {num2}?"
        ]
        
        index = random.randint(0, len(prompts) - 1)
        prompt = prompts[index]
        
        # Calculate answer directly instead of using eval()
        if index == 0:
            answer = num1
            answer = answer + num2 if sign1 == '+' else answer - num2
            answer = answer + num3 if sign2 == '+' else answer - num3
        else:
            answer = num3
            answer = answer + num2 if sign2 == '+' else answer - num2
        
        answers = [
            answer,
            answer + random.randint(1, 5),
            answer - random.randint(1, 5),
            answer + random.randint(6, 10)
        ]
        random.shuffle(answers)
        answer_index = answers.index(answer)
        
        f_answer = [f"{self.letters[i]}) {answers[i]}" for i in range(len(answers))]
        
        f_prompt = f"""{prompt}\nAnswers:\n{"\n".join(f_answer)}"""
        
        return f_prompt, answer_index