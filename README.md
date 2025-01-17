# Computer Science Quiz Application

A simple command-line quiz application built in Python that tests users' knowledge of computer science concepts through true/false questions.

## Description

This application presents users with a series of computer science-related questions. It keeps track of the user's score and provides immediate feedback after each answer. Questions cover various topics including programming languages, computer hardware, and technology history.

## Features

- Multiple-choice true/false questions
- Immediate feedback on answers
- Score tracking throughout the quiz
- Final score display upon completion
- Questions of varying difficulty levels (easy, medium, hard)

## Project Structure

The project consists of four main Python files:

- `data.py`: Contains the question database
- `question_model.py`: Defines the Question class structure
- `quiz_brain.py`: Contains the quiz logic and scoring system
- `main.py`: The entry point of the application

## Installation

1. Clone the repository to your local machine
2. Ensure you have Python 3.x installed
3. No additional dependencies are required

## Usage

To run the quiz:

```bash
python main.py
```

Follow the prompts and input either "True" or "False" for each question.

## Classes

### Question

- Stores individual question data
- Attributes:
  - `text`: The question text
  - `answer`: The correct answer

### QuizBrain

- Manages the quiz logic
- Methods:
  - `still_has_questions()`: Checks if there are remaining questions
  - `next_question()`: Presents the next question
  - `check_answer()`: Validates user input and updates score

### PrintFinalInfo

- Handles the display of final quiz results
- Methods:
  - `display()`: Shows the final score and completion message

## Sample Questions

The quiz includes questions about:

- HTML5 standards
- Linux and Git
- Programming language concepts
- Computer hardware
- And more...

## Contributing

Feel free to submit issues and enhancement requests or fork the repository and submit pull requests with improvements.
