"""
Should generate an arithmetic problem involving addition and subtraction.
Returns: A prompt and its answer's index.
"""
import random

class ArithmeticQuestion:
    @staticmethod
    def get_arithmetic_question():
        nums = random.sample(range(2, 39), 3)
        num1, num2, num3 = nums[0], nums[1], nums[2]
        
        letters = ["A", "B", "C", "D"]
        f_answer = []
        
        signs = ['+', '-']
        sign1 = random.choice(signs)
        sign2 = random.choice(signs)
        
        prompts = [
            f"What is {num1} {sign1} {num2} {sign2} {num3}?",
            f"What is {num3} {sign2} {num2}?"
        ]
        
        index = random.randint(0, len(prompts) - 1)
        prompt = prompts[index]
        answer = eval(prompt.split("What is ")[1].replace('?', ''))
        
        answers = [
            answer,
            answer + random.randint(1, 5),
            answer - random.randint(1, 5),
            answer + random.randint(6, 10)
        ]
        random.shuffle(answers)
        answer_index = answers.index(answer)
        
        for i in range(len(answers)):
            f_answer.append(f"{letters[i]}) {answers[i]}")
        
        f_prompt = f"""{prompt}
Answers:
{"\n".join(f_answer)}
"""
        
        return f_prompt, answer_index