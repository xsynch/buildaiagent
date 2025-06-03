import os 


def overwrite_file(working_directory, file_path, content):
    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    full_path = os.path.join(working_directory,file_path)
    if not os.path.exists(full_path):
        dirname,_ = os.path.split(full_path)
        os.makedirs(dirname,exist_ok=True)
    with open(full_path,"w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} bytes written)'