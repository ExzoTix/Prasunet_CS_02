from tkinter import Tk, filedialog, simpledialog
from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key=42):
    try:
        # Open the image
        img = Image.open(image_path)
        img_array = np.array(img)

        # Encrypt: Add the key to each pixel value
        encrypted_array = (img_array.astype('int16') + key) % 256
        
        # Ensure the data type is 'uint8'
        encrypted_array = encrypted_array.astype('uint8')
        
        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(encrypted_image_path, output_path, key=42):
    try:
        # Open the encrypted image
        encrypted_img = Image.open(encrypted_image_path)
        encrypted_array = np.array(encrypted_img)
        
        # Decrypt: Subtract the key from each pixel value
        decrypted_array = (encrypted_array.astype('int16') - key) % 256
        
        # Ensure the data type is 'uint8'
        decrypted_array = decrypted_array.astype('uint8')
        
        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def select_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def save_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    return file_path

def get_key():
    root = Tk()
    root.withdraw()
    key = simpledialog.askinteger("Input", "Enter the encryption key (an integer between 0 and 255):", minvalue=0, maxvalue=255)
    return key
  
# Get the input paths and key from the user
image_path = select_file()
encrypted_image_path = select_file()
encrypted_path = save_file()
decrypted_path = save_file()
key = get_key() % 256

# Encrypt the image
encrypt_image(image_path, encrypted_path, key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_path, key)
