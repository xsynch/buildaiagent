from google import genai 
from google.genai import types 


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get file content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The content of the file, relative to the working directory.",
            ),
        },
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python script, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to execute, relative to the working directory.",
            ),

        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="overwrite_file",
    description="Overwite the contents of a file. Constrained by working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to overwite and the contents, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            )
        },
    ),
)
