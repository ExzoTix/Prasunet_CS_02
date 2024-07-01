# TASK-02 Pixel Manipulation for Image Encryption
- In this task, we have to develop a simple image encryption tool using pixel manipulation. We can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Moreover, we should allow users to encrypt and decrypt images.
- Here we have applied basic mathematical operation like Addition to each pixel for Encryption and Subtraction to each pixel for Decryption.
- Please find the Python program named as **image_encryption.py** and two example images named as **image.png** and **decrypted_image.png** attached.

# Pixel manipulation
Pixel manipulation in image encryption involves altering the pixel values of an image to transform it into an encrypted or unreadable format, with the intention of securing the image content against unauthorized access or tampering. This process is crucial in various applications such as secure image transmission, digital watermarking, and privacy protection.

**Key Concepts of Pixel Manipulation in Image Encryption**

1. **Pixel Value Transformation**:
   - Each pixel in an image has a value corresponding to its color and intensity. In pixel manipulation, these values are altered using various cryptographic techniques to create an encrypted version of the image.

2. **Substitution**:
   - Pixel values are replaced or substituted with other values according to a predefined key or algorithm. This can be done in a way that the original pixel values are not recognizable.

3. **Permutation**:
   - The positions of pixels are shuffled according to a key, making it difficult to determine the original image. This does not change the pixel values but rearranges their positions.

4. **Bit-Level Manipulation**:
   - Alterations are made at the bit level of the pixel values, such as flipping certain bits according to a key. This approach can provide a high level of security with minimal perceptible changes in the image.

5. **Diffusion and Confusion**:
   - **Diffusion**: Spreads out the influence of a single pixel over many pixels in the encrypted image, making it difficult to trace the original pixel value.
   - **Confusion**: Ensures that the relationship between the original and encrypted pixel values is complex and non-linear, making it hard to infer the original image.

 **Techniques Used in Pixel Manipulation for Image Encryption**

1. **XOR Encryption**:
   - Each pixel value is combined with a key using the XOR operation. This is simple yet effective, especially when the key is kept secret.
  
2. **Arnold Cat Map**:
   - A chaotic map that scrambles the pixels of an image. It uses a specific formula to permute the positions of pixels, making the image appear disordered.

3. **Chaos-Based Encryption**:
   - Utilizes chaotic systems to generate pseudo-random sequences that determine how pixel values are manipulated. These systems are sensitive to initial conditions, which makes them suitable for secure encryption.

4. **Color Channel Manipulation**:
   - In color images, different channels (Red, Green, Blue) are encrypted separately or in combination, adding complexity to the encryption process.

5. **Image Scrambling**:
   - Shuffling the rows and columns of an image based on a key or algorithm to obscure the original content.

6. **Logistic Map Encryption**:
   - Uses logistic maps to generate sequences for encrypting pixel values. The logistic map is a simple mathematical model that exhibits chaotic behavior.

**Applications**

- **Secure Image Transmission**: Protecting images sent over networks from unauthorized access.
- **Digital Watermarking**: Embedding information into images for copyright protection.
- **Privacy Protection**: Ensuring sensitive images are not accessible to unauthorized users.
