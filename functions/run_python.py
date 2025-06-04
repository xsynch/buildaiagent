import os, subprocess

def run_python_file(working_directory, file_path):
    full_path = os.path.join(working_directory,file_path)
    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    _,filename = os.path.split(full_path)
    if not filename.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        results = ""
        # print(f"Full Path: {full_path}")
        completed_process = subprocess.run(["python",file_path],capture_output=True,timeout=30,cwd=working_directory)
        if completed_process.returncode != 0:
            results += f"Process exited with code {completed_process.returncode}\n"
        if not completed_process.stdout:
            results += f"No output produced\n"
        results += f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
        return results
    
    except Exception as e:
        return f"Error: executing Python file: {e}"