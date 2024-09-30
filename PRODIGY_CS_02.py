# Image Encryption Tool
from PIL import Image


# Function to encrypt image
def encrypt_image(image_path, message, key):
    image = Image.open(image_path) #Opens image
    width, height = image.size
    pixels = list(image.getdata())

    # Convert message to a numerical rep
    message_values = [ord(c) for c in message]

    # Encrypt the image by adding the message values to each pixel
    encrypted_pixels = []
    for i, pixel in enumerate(pixels):
        r, g, b = pixel
        r = (r + message_values[i % len(message_values)] + key) % 256
        g = (g + message_values[i % len(message_values)] + key) % 256
        b = (b + message_values[i % len(message_values)] + key) % 256
        encrypted_pixels.append((r, g, b))

    # Save the encrypted image
    encrypted_image = Image.new('RGB', (width, height))
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save('encrypted_image.png')

# Function to decrypt an image
def decrypt_image(image_path, key):
    image = Image.open(image_path) # Open the encrypted image
    width, height = image.size
    pixels = list(image.getdata())

    # Decrypt the image by subtracting the key from each pixel
    decrypted_pixels = []
    for pixel in pixels:
        r, g, b = pixel
        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256
        decrypted_pixels.append((r, g, b))

    # Extract the original message from the decrypted image
    message_values = []
    for i, pixel in enumerate(decrypted_pixels):
        r, g, b = pixel
        message_values.append((r + g + b) % 256)
    message = ''.join([chr(c) for c in message_values])

    return message

def main():
    image_path = input("Enter the path to the original image: ")
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the encryption key: "))

    # Encrypt the image
    encrypt_image(image_path, message, key)
    print("Encrypted image saved as 'encrypted_image.png'")

    # Decrypt the image
    decrypted_message = decrypt_image('encrypted_image.png', key)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()