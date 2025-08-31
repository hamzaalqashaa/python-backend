from PIL import Image, ImageFilter

# Load an image
try:
    image = Image.open("sample.jpeg")
except FileNotFoundError:
    print("Image not found. Please make sure 'sample.jpeg' is in the same directory.")
    exit()

# Apply filters
blurred = image.filter(ImageFilter.BLUR)
contour = image.filter(ImageFilter.CONTOUR)
embossed = image.filter(ImageFilter.EMBOSS)

# Create collage
width, height = image.size
collage = Image.new("RGB", (width * 2, height * 2), "white")

collage.paste(image, (0, 0))
collage.paste(blurred, (width, 0))
collage.paste(contour, (0, height))
collage.paste(embossed, (width, height))

# Save the collage
collage.save("extras/image_collage.jpeg")
print("Collage saved as 'image_collage.jpeg'")
