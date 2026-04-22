## File Organizer (Python)

A simple Python script to automatically organize files in a directory by their file type (extension).  
Each file type gets its own folder, making the directory clean and structured.

---

##  Features
- Scans a base directory for files
- Detects file extensions
- Creates folders named after each extension (e.g., `PDF`, `TXT`, `JPG`)
- Moves files into their respective folders
- Skips duplicates if the file already exists in the destination

---

##  Usage
1. Set the `base_path` variable to the folder you want to organize:
   ```python
   base_path = r"C:\Users\admin\abc"

# Before
abc/
 |--- report.pdf
 |--- notes.txt
 |--- image.jpg

# After running the code
abc/
 |--- PDF/report.pdf
 |--- TXT/notes.txt
 |--- JPG/image.jpg
