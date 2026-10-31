# Laptop Storage Cleanup Advisor

## 1. Project Title

**Laptop Storage Cleanup Advisor**

## 2. Problem Statement

It can be difficult to tell which files are using space in a folder. This console program scans one folder, totals the file sizes, groups files by type, and points out the largest files.

## 3. Objective

The objective is to practice basic Python by building a small tool that helps a user understand folder storage and decide what they may want to review.

**The program only analyzes files and provides suggestions. It does not automatically delete files.**

## 4. Features

- Ask the user for a folder path and check that it is a folder.
- List files directly inside that folder with their names, paths, sizes, and extensions.
- Find matching numbered copies such as `report.pdf`, `report1.pdf`, and `report (1).pdf` when their sizes are equal.
- Calculate total storage and storage by category.
- Show up to five largest files.
- Give simple suggestions when a category uses at least 1 GB or a file is larger than 1 GB.
- Continue scanning if an individual file cannot be accessed.
- Never delete or change files.

## 5. Technologies Used

- Python 3
- Python standard library: `os`
- Console input and output

No external packages are needed.

## 6. Python Concepts Used

- Variables and strings
- Lists and dictionaries
- Functions and modules
- `if` / `elif` / `else` conditions
- `for` loops and a `while` loop
- File and folder handling with `os`
- Sorting a list by file size

## 7. Project Structure

```text
Laptop-Storage-Cleanup-Advisor/
├── main.py
├── scanner.py
├── duplicate.py
├── analyzer.py
├── report.py
├── suggestions.py
└── README.md
```

- `main.py` asks for the folder and connects the other modules.
- `scanner.py` reads file details from the selected folder.
- `duplicate.py` finds and displays numbered-name matches with the same file size.
- `analyzer.py` calculates totals, categories, and file-size order.
- `suggestions.py` creates review suggestions.
- `report.py` prints the results.
- `README.md` explains the project and how to run it.

## 8. How the Program Works

1. `main.py` asks for a folder path and checks that it exists and is a folder.
2. `scanner.py` checks the files directly inside it. For each accessible file, it records the name, path, size in bytes, and lowercase extension.
3. `duplicate.py` groups files whose names share a base name, where at least one name ends in a number, and whose sizes match.
4. `analyzer.py` adds file sizes, totals categories, and sorts files by size.
5. `suggestions.py` checks category totals and file sizes for large-storage suggestions.
6. `report.py` displays folder information, the storage summary, category totals, the largest files, duplicate-file results, and cleanup suggestions.

Files inside subfolders are not scanned.

## 9. How to Run

1. Open this project folder in VS Code.
2. Open the integrated terminal in the project folder.
3. Run:

   ```text
   python main.py
   ```

4. Enter the path to the folder you want to analyze. A path with spaces can be entered with or without surrounding quotes.

## 10. Example Output

For a test folder with these file sizes:

| File | Size used in test |
|---|---:|
| `movie.mp4` | 4 KB |
| `photo.jpg` | 2 KB |
| `notes.pdf` | 1 KB |
| `project.zip` | 3 KB |
| `setup.exe` | 5 KB |
| `document.txt` | 512 B |

The total is 15.50 KB. The program should display output similar to this (the folder path will depend on where the test folder is created):

```text
========================================
      LAPTOP STORAGE CLEANUP ADVISOR
========================================

Scanning files...

Analysis completed!

[1] Folder Information
Folder Path : <test folder path>
Files Found : 6

[2] Storage Summary
Total Size  : 15.50 KB

[3] Category Analysis

Videos      : 4.00 KB
Images      : 2.00 KB
Documents   : 1.50 KB
Archives    : 3.00 KB
Programs    : 5.00 KB
Other       : 0 B

------------------------------------

[4] Largest Files (Top 5)

1. setup.exe - 5.00 KB
2. movie.mp4 - 4.00 KB
3. project.zip - 3.00 KB
4. photo.jpg - 2.00 KB

------------------------------------

[5] Cleanup Suggestions

Thank you for using the program.
```

## 11. Limitations

- Only the selected folder's direct files are scanned; subfolders are not included.
- The program reports sizes in binary units: 1 KB is 1024 bytes, 1 MB is 1024 KB, and 1 GB is 1024 MB.
- It categorizes files using a short, fixed list of extensions. Other extensions are put in `Other`.
- Category suggestions start at 1 GB, and the very-large-file suggestion is for files larger than 1 GB.
- It does not decide whether a file is safe to remove.
- A file that cannot be accessed is skipped with a message.

## 12. Future Improvements

- Add an optional way to include subfolders.
- Let the user choose a different threshold for large files.
- Add more common file extensions to the categories.
- Allow saving a text copy of the report, with the user's permission.

## Test Scenarios

These are the simple cases used to check the program:

1. **Valid folder:** Scan the six example files above and check that all six are counted and the total is 15.50 KB.
2. **Invalid folder:** Enter a path that does not exist. The program should show an error and stop without showing a storage report.
3. **Empty folder:** Scan an existing folder with no files. It should show zero files, total size `0 B`, zero bytes for each category, and `No files found.` under largest files.
4. **Unknown file types:** Put `mystery.xyz` and a file with no extension in a folder. Both should be counted under `Other`.
5. **Different file sizes:** Check the sample folder's largest-file list. `setup.exe` should appear before `movie.mp4`, which should appear before `project.zip`.
6. **Files needing a suggestion:** A category total of at least 1 GB should produce its category suggestion. A file larger than 1 GB should produce the very-large-file suggestion.
All tests only read file information. No files are deleted or modified.
