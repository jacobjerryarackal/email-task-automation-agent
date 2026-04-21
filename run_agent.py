import argparse
from agent.email_agent import process_email

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to email file")
    args = parser.parse_args()

    with open(args.input, "r") as file:
        email_text = file.read()

    result = process_email(email_text)

    print("\n=== OUTPUT ===\n")
    print(result)


if __name__ == "__main__":
    main()