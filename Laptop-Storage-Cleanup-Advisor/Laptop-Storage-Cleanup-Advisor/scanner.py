import os


def scan_folder(folder_path):
    """Return basic information about files directly inside a folder."""
    if not os.path.exists(folder_path):
        print("Error: The folder does not exist.")
        return None

    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a folder.")
        return None

    files = []

    try:
        with os.scandir(folder_path) as folder_entries:
            for entry in folder_entries:
                try:
                    if entry.is_file(follow_symlinks=False):
                        file_size = entry.stat(follow_symlinks=False).st_size
                        file_information = {
                            "name": entry.name,
                            "path": entry.path,
                            "size": file_size,
                            "extension": os.path.splitext(entry.name)[1].lower(),
                        }
                        files.append(file_information)
                except OSError as error:
                    print("Could not access " + entry.path + ": " + str(error))
    except OSError as error:
        print("Error: Could not scan the folder: " + str(error))
        return None

    return files