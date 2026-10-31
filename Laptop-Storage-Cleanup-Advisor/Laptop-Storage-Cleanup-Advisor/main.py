import os

import analyzer
import duplicate
import report
import scanner
import suggestions


def get_folder_path():
    """Ask for a folder and return it only if it is a valid directory."""
    folder_path = input("Enter folder path:\n").strip().strip('"')

    if not os.path.exists(folder_path):
        print("Error: The folder does not exist.")
        return None

    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a folder.")
        return None

    return folder_path


def main():
    print("========================================")
    print("      LAPTOP STORAGE CLEANUP ADVISOR")
    print("========================================")
    print()

    folder_path = get_folder_path()
    if folder_path is None:
        return

    print()
    print("Scanning files...")
    files = scanner.scan_folder(folder_path)

    if files is None:
        return

    duplicate_groups = duplicate.find_duplicates(files)

    total_size = analyzer.calculate_total_size(files)
    category_storage = analyzer.calculate_category_storage(files)
    largest_files = analyzer.find_largest_files(files)
    cleanup_suggestions = suggestions.generate_suggestions(
        category_storage, largest_files
    )

    print()
    print("Analysis completed!")
    report.display_report(
        folder_path,
        files,
        total_size,
        category_storage,
        largest_files,
        cleanup_suggestions,
        duplicate_groups,
    )

    print()
    print("Thank you for using the program.")


if __name__ == "__main__":
    main()