from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        image_array = np.array(image)

        np.random.seed(key)
        random_indices = np.random.permutation(image_array.size)

        flattened = image_array.flatten()
        encrypted_flat = flattened[random_indices]

        encrypted_image = encrypted_flat.reshape(image_array.shape)
        Image.fromarray(encrypted_image).save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        image_array = np.array(image)

        np.random.seed(key)
        random_indices = np.random.permutation(image_array.size)

        flattened = image_array.flatten()
        decrypted_flat = np.empty_like(flattened)
        decrypted_flat[random_indices] = flattened

        decrypted_image = decrypted_flat.reshape(image_array.shape)
        Image.fromarray(decrypted_image).save(output_path)
        print(f"Image decrypted and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1/2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice!")
        exit()

    input_path = input("Enter the path of the image file: ")
    output_path = input("Enter the output path for the image: ")
    key = int(input("Enter an encryption/decryption key (integer): "))

    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)
