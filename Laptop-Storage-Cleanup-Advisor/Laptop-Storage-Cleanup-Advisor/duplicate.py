import os


def names_match(first_name, second_name):
    """Check for names like photo.jpg and photo1.jpg."""
    first_base, first_extension = os.path.splitext(first_name)
    second_base, second_extension = os.path.splitext(second_name)

    if first_extension.lower() != second_extension.lower():
        return False

    first_base = first_base.lower()
    second_base = second_base.lower()

    if second_base.startswith(first_base):
        extra_text = second_base[len(first_base):]
        if extra_text.strip(" ()-_").isdigit():
            return True

    if first_base.startswith(second_base):
        extra_text = first_base[len(second_base):]
        if extra_text.strip(" ()-_").isdigit():
            return True

    return False


def find_duplicates(files):
    """Find same-size files with matching numbered names."""
    groups = []

    for file_information in files:
        found_group = False

        for group in groups:
            for other_file in group:
                same_size = file_information["size"] == other_file["size"]
                same_name = names_match(
                    file_information["name"], other_file["name"]
                )

                if same_size and same_name:
                    group.append(file_information)
                    found_group = True
                    break

            if found_group:
                break

        if not found_group:
            groups.append([file_information])

    return [group for group in groups if len(group) > 1]


def display_duplicates(duplicate_groups):
    """Print matching file names and sizes."""
    if not duplicate_groups:
        print("No duplicate files found.")
        return

    print("Duplicate files found!")

    for group_number, group in enumerate(duplicate_groups, start=1):
        print()
        print("Duplicate Group " + str(group_number) + ":")

        for file_information in group:
            print(
                file_information["name"]
                + " - "
                + str(file_information["size"])
                + " bytes"
            )
