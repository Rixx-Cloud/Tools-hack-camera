from PIL import Image

def compress_image(input_path, output_path, quality=85):
    """Kompres gambar tanpa merusak privasi."""
    try:
        img = Image.open(input_path)
        img.save(output_path, optimize=True, quality=quality)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Contoh penggunaan:
# compress_image("input.jpg", "output.jpg")
