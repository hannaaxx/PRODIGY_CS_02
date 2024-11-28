
# Image Encryption Tool

A simple tool to encrypt and decrypt images using pixel manipulation techniques.

## Features
- **Encrypt Images:** Transform pixel values using a user-defined key.
- **Decrypt Images:** Reconstruct the original image using the same key.
- **Supports Various Formats:** Works with popular image formats like PNG, JPEG, and BMP.

---

## Prerequisites
- Python 3.x
- Required Libraries:
  - `Pillow` (for image processing)
  - `numpy` (for array manipulations)

Install the required libraries using:
```bash
pip install pillow numpy
How to Use
Clone or download this repository.

Run the script using:

bash
Copy code
python image_encryption_tool.py
Choose an option:

Encrypt Image: Provide an input image, output path, and an integer key.
Decrypt Image: Use the encrypted image, output path, and the same key for decryption.
Example Usage
Encrypting an Image:
Place the image in the project directory.
Run the script and select 1 for encryption.
Provide the image path (e.g., image.png), output path (e.g., encrypted_image.png), and a key (e.g., 1234).
Decrypting an Image:
Use the encrypted image generated earlier.
Run the script and select 2 for decryption.
Provide the encrypted image path, output path (e.g., decrypted_image.png), and the same key used for encryption.
Notes
The key is essential for decryption. Without it, the image cannot be decrypted.
Ensure that the input image file exists and is accessible.
Always use the same key for encryption and decryption.
License
This project is licensed under the MIT License.

yaml
Copy code

---

### How It Works
1. The script flattens the image into a one-dimensional array.
2. A random permutation based on the user-provided key rearranges the pixels during encryption.
3. For decryption, the script reverses the process using the same key to reconstruct the original order.

Let me know if you need additional explanations or improvements!





