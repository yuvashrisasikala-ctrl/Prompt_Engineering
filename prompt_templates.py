def build_prompt(technique, task):

    if technique == "Zero-shot":
        return task.strip()

    elif technique == "One-shot":
        return f"""
Example:
Question: What is AI?
Answer: AI enables computers to perform tasks that usually require human intelligence.

Question: {task}
Answer:
""".strip()

    elif technique == "Few-shot":
        return f"""
Example 1:
Question: What is Python?
Answer: Python is a programming language.

Example 2:
Question: What is Java?
Answer: Java is an object-oriented programming language.

Question: {task}
Answer:
""".strip()

    elif technique == "CoT":
        return f"""
Answer the following question carefully.
Explain the key steps briefly and provide the final answer.

Question: {task}
Answer:
""".strip()

    elif technique == "Manual CoT":
        return f"""
Answer the question using these steps:
1. Understand the question.
2. Identify the important points.
3. Prepare a clear answer.
4. Give a suitable example if needed.

Question: {task}
Answer:
""".strip()

    elif technique == "ToT":
        return f"""
Consider different possible approaches to answering the question.
Choose the most suitable approach and provide a clear final answer.

Question: {task}
Answer:
""".strip()

    return task.strip()