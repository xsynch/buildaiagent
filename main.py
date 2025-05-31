import os, sys
from dotenv import load_dotenv
from google import genai

def main(userInputs: list[str]):
    prompt = userInputs[1]
    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),
    ]


    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
    if(userInputs[len(userInputs)-1]) == "--verbose":
        print(f"Working on: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # print("Please include a prompt")
        sys.exit("Please include a prompt")    
    main(sys.argv)