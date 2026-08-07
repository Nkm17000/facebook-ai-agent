prompt = """
Generate a premium English Mock Test for **{Exam Name}**.

Create a completely NEW and UNIQUE test every time. Never repeat questions, vocabulary, grammar rules, idioms, phrasal verbs, passages, examples, answer choices, or question patterns from previous tests.

Requirements:
- Generate at least 10 multiple-choice questions.
- Four options (A–D) with exactly one correct answer.
- Match the latest syllabus, pattern, and difficulty of {Exam Name}.
- Questions should resemble real SSC, UPSC, Banking, Railway, CDS, CAPF, or State PSC exams.
- Prefer previous-year inspired, concept-based, and application-oriented questions.
- Keep questions concise, clear, and exam-oriented.

Randomly select questions from different English topics, including:
- Reading Comprehension
- Cloze Test
- Fill in the Blanks
- Error Detection
- Sentence Improvement
- Para Jumbles
- Active & Passive Voice
- Direct & Indirect Speech
- Tenses
- Subject-Verb Agreement
- Articles
- Prepositions
- Conjunctions
- Modals
- Pronouns
- Adjectives & Adverbs
- Synonyms
- Antonyms
- Idioms & Phrases
- Phrasal Verbs
- One Word Substitution
- Spelling Correction
- Vocabulary
- Phrase Replacement
- Spot the Error
- Miscellaneous Grammar

Ensure:
- Every test covers a balanced mix of topics.
- Vary the difficulty (Easy, Medium, Hard).
- Randomize question order and topic distribution.
- Use different question styles in every test.
- Avoid predictable patterns.
- Use modern and exam-relevant contexts.

Output Format:

📘 English Mock Test – {Exam Name}

Q1.
Question

A.
B.
C.
D.

...

Q10.
Question

A.
B.
C.
D.

━━━━━━━━━━━━━━━━━━━━━━

✅ Answer Key & Explanation

1. B – One-line explanation.
2. D – One-line explanation.
...
10. A – One-line explanation.

Return ONLY the mock test and answer key.
"""