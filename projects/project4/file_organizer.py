import os
import shutil

# Mapping of file extensions to folder names
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []  # fallback category
}


def get_category(extension):
    """Return category name based on file extension."""
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_files(directory):
    """Organize files in the given directory into subfolders by type."""
    if not os.path.exists(directory):
        print("❌ Directory does not exist.")
        return

    # Iterate through files only (ignore subfolders for safety)
    for entry in os.scandir(directory):
        if entry.is_file():
            filename, extension = os.path.splitext(entry.name)
            category = get_category(extension)

            # Create category folder if it doesn't exist
            category_folder = os.path.join(directory, category)
            os.makedirs(category_folder, exist_ok=True)

            # Move file
            dest_path = os.path.join(category_folder, entry.name)
            shutil.move(entry.path, dest_path)
            print(f"✅ Moved: {entry.name} → {category}/")

    print("\n🎉 Organization complete!")


def main():
    print("📂 Automated File Organizer")
    directory = input("Enter the directory to organize: ").strip()
    organize_files(directory)


if __name__ == "__main__":
    main()
