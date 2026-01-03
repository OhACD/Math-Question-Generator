"""
Should generate a word problem involving the purchase of fruits.
Returns: A prompt and its answer's index.
"""
import random

class WordQuestion:
    def __init__(self, names, min, max):
        self.names = names
        self.min = min
        self.max = max
        self.letters = ["A", "B", "C", "D"]
    
    def get_word_question(self):
        name = random.choice(self.names)
        
        # Lazy generate numbers to allow lower number ranges without bugs
        values1 = random.sample(range(self.min, self.max), 2)
        values2 = random.sample(range(self.min, self.max), 2)
        num_apples, num_bananas, price_apples, price_bananas = values1[0], values1[1], values2[0], values2[1]
        total_cost = (num_apples * price_apples) + (num_bananas * price_bananas)
        
        answers = [
            total_cost,
            total_cost + random.randint(1, 5),
            total_cost - random.randint(1, 5),
            total_cost + random.randint(6, 10)
        ]
        random.shuffle(answers)
        
        f_answers = [f"{self.letters[i]}) ${answers[i]}" for i in range(len(answers))]
        
        prompt = f"""
{name} wants to buy {num_apples} apples for ${price_apples} each and {num_bananas} bananas for ${price_bananas} each.
How much will {name} spend in total?
Answers:
{"\n".join(f_answers)}
"""
        
        return prompt, answers.index(total_cost)


