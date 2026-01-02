"""
Should generate a word problem involving the purchase of fruits.
Returns: A prompt and its answer's index.
"""
import random

class WordQuestion:
    @staticmethod
    def get_word_question():
        names = ["Alice", "Bob", "Charlie", "Diana"]
        letters = ["A", "B", "C", "D"]
        f_answers = []
        name = random.choice(names)
        num_apples = random.randint(2, 6)
        price_apples = random.randint(1, 5)
        num_bananas = random.randint(2, 6)
        price_bananas = random.randint(1, 5)
        total_cost = (num_apples * price_apples) + (num_bananas * price_bananas)
        
        answers = [
            total_cost,
            total_cost + random.randint(1, 5),
            total_cost - random.randint(1, 5),
            total_cost + random.randint(6, 10)
        ]
        random.shuffle(answers)
        
        for i in range(len(answers)):
            f_answers.append(f"{letters[i]}) ${answers[i]}")
        
        
        prompt = f"""{name} want's to by {num_apples} apples for ${price_apples} each and {num_bananas} bananas for ${price_bananas} each. How much will {name} spend in total?
Answers:
{"\n".join(f_answers)}
"""
        
        return prompt, answers.index(total_cost)


