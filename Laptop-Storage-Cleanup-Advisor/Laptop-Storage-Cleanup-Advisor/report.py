import duplicate


def format_size(size_in_bytes):
    """Convert a byte count to B, KB, MB, or GB."""
    size = float(size_in_bytes)
    units = ["B", "KB", "MB", "GB"]
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size = size / 1024
        unit_index += 1

    if unit_index == 0:
        return str(int(size)) + " " + units[unit_index]

    return "{:.2f} {}".format(size, units[unit_index])


def display_report(
    folder_path,
    files,
    total_size,
    category_storage,
    largest_files,
    cleanup_suggestions,
    duplicate_groups=None,
):
    if duplicate_groups is None:
        duplicate_groups = []

    print()
    print("[1] Folder Information")
    print("Folder Path : " + folder_path)
    print("Files Found : " + str(len(files)))
    print()
    print("[2] Storage Summary")
    print("Total Size  : " + format_size(total_size))
    print()
    print("[3] Category Analysis")
    print()

    category_names = [
        "Videos",
        "Images",
        "Documents",
        "Archives",
        "Programs",
        "Other",
    ]

    for category in category_names:
        category_size = format_size(category_storage[category])
        print("{:<12}: {}".format(category, category_size))

    print()
    print("------------------------------------")
    print()
    print("[4] Largest Files (Top 5)")
    print()

    if len(largest_files) == 0:
        print("No files found.")
    else:
        file_number = 1
        for file_information in largest_files[:5]:
            file_size = format_size(file_information["size"])
            print(
                str(file_number) + ". "
                + file_information["name"] + " - " + file_size
            )
            file_number += 1

    print()
    print("------------------------------------")
    print()
    duplicate.display_duplicates(duplicate_groups)
    print()
    print("------------------------------------")
    print()
    print("[5] Cleanup Suggestions")
    print()

    if len(cleanup_suggestions) == 0:
        print("No specific cleanup suggestions. Your folder looks manageable.")
    else:
        for suggestion_number, suggestion in enumerate(cleanup_suggestions, start=1):
            suggestion_lines = suggestion.splitlines()
            print(str(suggestion_number) + ". " + suggestion_lines[0])
            for suggestion_line in suggestion_lines[1:]:
                print(suggestion_line)