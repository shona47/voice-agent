from app.tools.memory_rag import retrieve_memory

questions = [
    "What model does my project use for image-based defect detection?",
    "What dataset does my project use for sensor data?",
    "Which model does my project use for sensor-based prediction?"
]

for question in questions:

    print("\n===================================")
    print("QUESTION:", question)

    result = retrieve_memory(question)

    print("\nANSWER:", result["message"])
    print("RETRIEVED MEMORIES:", result.get("retrieved_memories"))