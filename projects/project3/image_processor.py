import os
from PIL import Image

# ---------------- Utility Functions ----------------
def get_image_files(input_dir):
    """Return a list of image file paths in the directory."""
    supported_ext = (".jpg", ".jpeg", ".png")
    return [os.path.join(input_dir, f) for f in os.listdir(input_dir)
            if f.lower().endswith(supported_ext)]


def save_image(img, output_dir, filename, suffix):
    """Save processed image to output directory with suffix."""
    os.makedirs(output_dir, exist_ok=True)
    base, ext = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{base}_{suffix}{ext}")
    img.save(output_path)
    print(f"✅ Saved: {output_path}")


# ---------------- Image Operations ----------------
def resize_images(input_dir, output_dir, width, height):
    """Resize all images in input_dir to given dimensions."""
    files = get_image_files(input_dir)
    for file in files:
        img = Image.open(file)
        resized = img.resize((width, height))
        save_image(resized, output_dir, os.path.basename(file), f"resized_{width}x{height}")


def grayscale_images(input_dir, output_dir):
    """Convert all images in input_dir to grayscale."""
    files = get_image_files(input_dir)
    for file in files:
        img = Image.open(file)
        gray = img.convert("L")
        save_image(gray, output_dir, os.path.basename(file), "grayscale")


def rotate_images(input_dir, output_dir, angle):
    """Rotate all images in input_dir by given angle."""
    files = get_image_files(input_dir)
    for file in files:
        img = Image.open(file)
        rotated = img.rotate(angle, expand=True)
        save_image(rotated, output_dir, os.path.basename(file), f"rotated_{angle}")


# ---------------- CLI Menu ----------------
def main():
    print("📸 Image Processing Utility")
    input_dir = input("Enter input directory path: ").strip()
    output_dir = input("Enter output directory path: ").strip()

    while True:
        print("\nChoose operation:")
        print("1. Resize Images")
        print("2. Convert to Grayscale")
        print("3. Rotate Images")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            resize_images(input_dir, output_dir, width, height)

        elif choice == "2":
            grayscale_images(input_dir, output_dir)

        elif choice == "3":
            angle = int(input("Enter rotation angle (degrees): "))
            rotate_images(input_dir, output_dir, angle)

        elif choice == "4":
            print("👋 Exiting Image Processor. Goodbye!")
            break

        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
