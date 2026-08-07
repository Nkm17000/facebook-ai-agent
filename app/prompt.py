prompt = """
Create a General Science quiz for **{Exam Name}**.

Generate **at least 10 multiple-choice questions** with four options (A–D) and exactly one correct answer for each.

Requirements:
- Match the latest syllabus, exam pattern, and difficulty level of the selected exam.
- Cover a balanced mix of Physics, Chemistry, Biology, Environmental Science, and Space Science unless a specific topic is requested.
- Prefer previous-year and concept-based questions.
- Avoid repeating questions.
- Keep questions concise, clear, and exam-oriented.

Output Format:

🧪 General Science Quiz – {Exam Name}

Q1. Question?
A. ...
B. ...
C. ...
D. ...

Q2. ...

...

Q10. ...

-------------------------
Answer Key
-------------------------

1. B
2. D
3. A
...

10. C

For each answer, provide a one-line explanation of why it is correct.

Return only the quiz and the answer key. Do not ask for user responses or provide interactive feedback.
"""