#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from teacher_assistant.crew import TeacherAssistant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # read notes from an argument or fallback to a sample file in knowledge/
    notes_path = sys.argv[1] if len(sys.argv) > 1 else "knowledge/lesson_notes_math.txt"
    if not os.path.isfile(notes_path):
        raise FileNotFoundError(f"Notes file not found: {notes_path}")

    with open(notes_path, "r", encoding="utf-8") as f:
        notes = f.read()
    inputs = {
        'topic': 'Introduction to Fractions',
        'current_year': str(datetime.now().year),
        'notes': notes
    }
    
    try:
        TeacherAssistant().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Introduction to Fractions",
        'current_year': str(datetime.now().year)
    }
    try:
        TeacherAssistant().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TeacherAssistant().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Introduction to Fractions",
        "current_year": str(datetime.now().year)
    }
    
    try:
        TeacherAssistant().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
