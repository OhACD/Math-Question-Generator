"""
Should generate a counting problem
Returns: A prompt and its answer's index.
"""
import random

class CountingQuestion:
    def __init__(self):
        self.letters = ["A", "B", "C", "D"]
        
    def get_counting_question(self):
        skip_values = [2, 3, 5, 10]
        skip_by = random.choice(skip_values)
        
        sequence_length = random.randint(3, 6)
        sequence = [skip_by * i for i in range(1, sequence_length + 1)]
        
        answer = skip_by * (sequence_length + 1)
        
        answers = [
            answer,
            answer + skip_by,
            answer - skip_by,
            answer + (2 * skip_by)
        ]
        
        random.shuffle(answers)
        answer_index = answers.index(answer)
        
        sequence_str = ", ".join(map(str, sequence))
        f_answers = [f"{self.letters[i]}) {answers[i]}" for i in range(len(answers))]
        
        prompt = f"What comes next in the sequence? {sequence_str}, ?\nAnswers:\n" + "\n".join(f_answers)
        
        return prompt, answer_index