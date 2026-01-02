# Math Question Generator

A Python CLI tool that generates math questions for elementary students (grades 4-6).

## Features

- **Arithmetic Questions**: Addition and subtraction problems with multiple choice answers
- **Word Problems**: Real-world scenarios involving money and simple calculations
- Random question generation for varied practice

## Installation

1. Clone this repository
2. Ensure you have Python 3.7+ installed

## Usage

Run the question generator from the `src` directory:

```bash
cd src
python question_generator.py
```

The tool will randomly generate either an arithmetic question or a word problem with multiple choice answers.

## Project Structure

```
math-question-generator/
├── src/
│   ├── question_generator.py    # Main entry point
│   └── questions/
│       ├── arithmetic.py         # Arithmetic question generator
│       └── word.py              # Word problem generator
└── README.md
```

## Future Plans

- Flask API wrapper for web access
- Simple frontend interface
- Additional question types (multiplication, division, fractions)
- Difficulty levels
- Question worksheets generation

## License

MIT
