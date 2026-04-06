import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configurable system prompt
SYSTEM_PROMPT = """You are an HR assistant that drafts professional offer letters.
Write a formal but warm offer letter using only the details provided.
Do not include any placeholder fields in brackets like [Company Name] or [Date].
If information is not provided, omit that section entirely — do not reference it.
Do not mention stock options if none were provided.
End the letter with just 'Sincerely,' and a blank line for a handwritten signature.
Format the letter with proper salutation, body paragraphs, and closing."""

def generate_offer_letter(candidate):
    user_message = f"""
    Please write an offer letter for the following candidate:
    
    Name: {candidate['name']}
    Position: {candidate['role']}
    Start Date: {candidate['start_date']}
    Base Salary: ${candidate['salary']:,}/year
    Bonus Eligibility: {candidate['bonus']}
    Stock Options: {candidate['stock_options']}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )

    return response.choices[0].message.content

def main():
    # Load candidate data
    with open("input.json", "r") as f:
        candidate = json.load(f)

    print("Generating offer letter...\n")
    letter = generate_offer_letter(candidate)

    # Print to console
    print("=" * 50)
    print("GENERATED OFFER LETTER")
    print("=" * 50)
    print(letter)
    print("=" * 50)

    # Save to file
    with open("output.txt", "w") as f:
        f.write(letter)

    print("\nOffer letter saved to output.txt")

if __name__ == "__main__":
    main()
