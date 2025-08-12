# CrewAI Teacher Assistant

This project implements a CrewAI-powered teacher assistant that reads lesson notes and automatically generates:

- A structured summary of the notes
- A detailed lesson plan
- A quiz based on the lesson
- Teaching suggestions and interactive activities

The assistant uses the **Gemini 1.5 Flash** model for generation tasks.

## Setup

1. Clone this repo and navigate into it.
2. Create a `.env` file with your API key(s), e.g.:
```bash
MODEL=gemini/gemini-1.5-flash
GEMINI_API_KEY="you-api-key"
```
3. Install dependencies:
```bash
crewai install
```
4. Place your lesson notes .txt files in src/teacher_assistant/knowledge/.

## Running the Crew
Run the assistant with:
```bash
crewai run
```

## Output Files
The following output files are generated (and included here as proof of assignment):

- lesson_plan.md — the generated lesson plan

- quiz.md — quiz questions with answers and difficulty

- suggestions.md — teaching tips and suggested activities

- parsed_notes.json — structured summary and key points

These files are saved in the project root by default.

---

Feel free to customize and extend this assistant for your educational projects!
