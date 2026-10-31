def get_category(extension):
    """Return the simple category name for a file extension."""
    extension = extension.lower()

    if extension in [".mp4", ".mkv", ".avi", ".mov"]:
        return "Videos"
    elif extension in [".jpg", ".jpeg", ".png", ".gif"]:
        return "Images"
    elif extension in [
        ".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"
    ]:
        return "Documents"
    elif extension in [".zip", ".rar", ".7z", ".tar"]:
        return "Archives"
    elif extension in [".exe", ".msi"]:
        return "Programs"
    else:
        return "Other"


def calculate_total_size(files):
    """Return the combined size of all files in bytes."""
    total_size = 0

    for file_information in files:
        total_size += file_information["size"]

    return total_size


def calculate_category_storage(files):
    """Return storage totals in bytes for each category."""
    category_storage = {
        "Videos": 0,
        "Images": 0,
        "Documents": 0,
        "Archives": 0,
        "Programs": 0,
        "Other": 0,
    }

    for file_information in files:
        category = get_category(file_information["extension"])
        category_storage[category] += file_information["size"]

    return category_storage


def get_file_size(file_information):
    """Return a file's size so files can be sorted by size."""
    return file_information["size"]


def find_largest_files(files):
    """Return the files sorted from largest to smallest."""
    return sorted(files, key=get_file_size, reverse=True)