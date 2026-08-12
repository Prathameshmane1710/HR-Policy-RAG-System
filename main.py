from hr_assistant.pipeline import ask,build_hr_assistant
from hr_assistant.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("=== CLI run started ===")
    print("Building the HR policy assistant...")
    agent = build_hr_assistant()
    print("Assistant ready!\n")

    demo_questions=[
        "How many paid annual leave days do I get?",
        "What is the notice period during probation?",
        "Can I work from home everyday?"
    ]

    for q in demo_questions:
        print("="*60)
        print("QUESTION:",q)
        print("="*60)
        answer = ask(agent,q)
        print("Answer",answer)
        print("="*60)
        print()

        logger.info("=== CLI run finished ===")

if __name__ == "__main__":
    main()
