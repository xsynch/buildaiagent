import os, sys
from dotenv import load_dotenv
from google import genai

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = genai.types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

def main(userInputs: list[str]):
    prompt = userInputs[1]
    # prompt = SYSTEM_PROMPT
    messages = [
        genai.types.Content(role="user", parts=[genai.types.Part(text=prompt)]),
    ]


    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    
    config=genai.types.GenerateContentConfig(
    tools=[available_functions], system_instruction=SYSTEM_PROMPT
    )

    response = client.models.generate_content(
        
        model='gemini-2.0-flash-001',contents=messages,config=config
    )
    if(userInputs[len(userInputs)-1]) == "--verbose":
        print(f"Working on: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls:
        fc = response.function_calls
        print(f"Calling function: {fc[0].name}({fc[0].args})")
    # print(response.text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # print("Please include a prompt")
        sys.exit("Please include a prompt")    
    main(sys.argv)