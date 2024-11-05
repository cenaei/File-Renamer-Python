File Renamer Script

Welcome! This simple Python script will help you batch rename files by
removing unwanted prefixes from file names. It’s particularly useful for
cleaning up file names downloaded with common prefixes like
\[SPOTDOWNLOADER.COM\].

Features

• Renames files by removing the specified prefix. • Easy to customize if
you want to change the prefix or use a different folder.

Prerequisites

• Python 3: Make sure Python 3 is installed on your system.

Getting Started

 1. Clone or download this repository: Download the script to your
preferred location. 2. Place files in the target folder: Ensure the
files you want to rename are located in a single folder.

Usage

 1. Open the script: Open file_renamer.py (or whatever name you choose
for this file) in a code editor. 2. Set the directory path: • Locate the
following line:

directory = "/path/to/your/files"

• Replace "/path/to/your/files" with the path to your folder that
contains the files to rename. Note: Use absolute paths for best results.

3. Run the script: • In the terminal, navigate to the directory where
the script is saved and execute:

python file_renamer.py

• The script will scan for files that start with the prefix
"\[SPOTDOWNLOADER.COM\] " and rename them by removing the prefix.

4. Check the Output: • Each renamed file will be printed to the console
as confirmation, e.g.,:

Renamed: "\[SPOTDOWNLOADER.COM\] a thousand years.mp3" to "a thousand
years.mp3"

Customization

1\. Changing the Prefix

• If you want to remove a different prefix (for example,
\[DOWNLOADSITE.COM\]), update this line:

if filename.startswith("\[SPOTDOWNLOADER.COM\] "):

• Replace "\[SPOTDOWNLOADER.COM\] " with the new prefix you wish to
remove.

2\. Changing the Directory Path

• Modify the directory variable to point to a different folder if you
want to rename files in another location:

directory = "/new/path/to/your/files"

Additional Notes

• Error Handling: The script currently assumes that all files in the
directory may have the prefix. If there are files without the prefix,
they’ll be ignored. • Undoing Changes: The script doesn’t keep a backup,
so be sure you want these changes before running it. For safety, test
with a few sample files if needed.

Example Output

Running this script with files like:

\[SPOTDOWNLOADER.COM\] a thousand years.mp3 \[SPOTDOWNLOADER.COM\]
beautiful day.mp3

Results in:

a thousand years.mp3 beautiful day.mp3

Feel free to reach out with any questions or suggestions for
improvement. Happy renaming!
