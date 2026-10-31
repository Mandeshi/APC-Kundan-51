def generate_suggestions(category_storage, largest_files):
    """Return simple review suggestions without changing any files."""
    suggestions = []
    large_storage_limit = 1024 * 1024 * 1024

    if category_storage["Videos"] >= large_storage_limit:
        suggestions.append(
            "Large amount of video files found. Review old videos."
        )

    if category_storage["Archives"] >= large_storage_limit:
        suggestions.append(
            "Large archive files found. Review old ZIP/RAR files."
        )

    if category_storage["Programs"] >= large_storage_limit:
        suggestions.append(
            "Large installation files found. Review old setup files."
        )

    for file_information in largest_files:
        if file_information["size"] > large_storage_limit:
            suggestions.append(
                "Very large files found. Review the largest files."
            )
            break

    return suggestions