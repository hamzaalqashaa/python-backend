from PIL import Image, ImageFilter

# Load an image
image = Image.open("sample.jpeg")
print(f"Original size: {image.size}")

# Resize
resized = image.resize((300, 300))
resized.save("resized.jpeg")
print("Resized image saved as resized.jpeg")

# Crop (left, upper, right, lower)
cropped = image.crop((50, 50, 300, 300))
cropped.save("cropped.jpeg")
print("Cropped image saved as cropped.jpeg")

# Apply blur filter
blurred = image.filter(ImageFilter.BLUR)
blurred.save("blurred.jpeg")
print("Blurred image saved as blurred.jpeg")

# Convert to grayscale
gray = image.convert("L")
gray.save("gray.jpeg")
print("Grayscale image saved as gray.jpeg")
