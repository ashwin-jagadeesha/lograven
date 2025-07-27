from lograven.qa.qa_engine import QAEngine

# Sample logs
log_data = [
    "2025-07-27 12:00:01 ERROR Failed to connect to database",
    "2025-07-27 12:00:02 INFO Retrying connection",
    "2025-07-27 12:00:03 Exception: ConnectionTimeout",
    "2025-07-27 12:00:04 INFO Connection established",
    "2025-07-27 12:00:05 CRITICAL System failure imminent",
    "2025-07-27 12:00:06 WARNING Disk space low"
]

# Initialize QA engine with local inference enabled
qa = QAEngine(use_inference=True)
qa.ingest_documents(log_data)

# Interactive loop
print("\n=== Log Q&A System ===")
print("Type your question or 'exit' to quit.\n")

while True:
    question = input("Ask a question about the logs:\n> ")
    if question.lower() in ["exit", "quit"]:
        print("bye")
        break

    answers = qa.answer(question)

    print("\nInference Answer:")
    print(answers[0])  # Inference answer (first item)

    print("\nTop Relevant Logs:")
    for i, ans in enumerate(answers[1:], 1):
        print(f"{i}. {ans}")

    print("\n" + "=" * 40 + "\n")
