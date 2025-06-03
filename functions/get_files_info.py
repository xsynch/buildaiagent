import os



def get_files_info(working_directory, directory=None):
    if directory is None or  directory.startswith("..") or  directory.startswith("/"):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'     
    result = ""
    full_dir = os.path.join(working_directory,directory)
    if not os.path.isdir(full_dir):
        return f'Error: "{directory}" is not a directory'
    for file in os.listdir(full_dir):
        # print(f"File or dir name: {file}")
        if os.path.isfile(os.path.join(full_dir,file)):
            result += f"- {file}: file_size={os.path.getsize(os.path.join(full_dir,file))} bytes, is_dir=False\n"
        elif os.path.isdir(os.path.join(full_dir,file)):            
            result += f"- {file}: file_size=0 bytes, is_dir=True\n"
        
    return result 

def get_file_content(working_directory, file_path):
    results = ""
    if file_path.startswith("..") or file_path.startswith("/"):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile((os.path.join(working_directory,file_path))):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(os.path.join(working_directory,file_path)) as f:
        
        character_count = 0
        for line in f:
            for character in line:
                if character_count >= 10000:
                    results += f'[...File "{file_path}" truncated at 10000 characters]'
                    return results 
                results += character
                character_count += 1
            
    return results
        