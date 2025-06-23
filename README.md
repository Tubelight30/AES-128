# AES-128 with Multi-Block Support

## Instruction for USE

- Clone the repository
- Run the aes_server.py file first and then run the aes_client.py file
- The Client will ask for the message and the key
- **NEW**: You can now enter messages of ANY LENGTH! The system will automatically handle padding and multi-block encryption.
- **Key Handling**: Enter the same key on both client and server sides. If the key is not exactly 16 characters, it will be automatically adjusted:
  - Keys shorter than 16 characters are padded with zeros
  - Keys longer than 16 characters are truncated to 16 characters
- Messages are now processed using PKCS#7 padding and ECB (Electronic Codebook) mode

## Features Added

- **Variable Length Messages**: No longer limited to 16 characters
- **PKCS#7 Padding**: Automatically pads messages to block boundaries
- **Multi-Block Processing**: Encrypts/decrypts messages in 16-byte blocks
- **Error Handling**: Better error handling for padding and decryption
- **Automatic Key Adjustment**: Keys are padded or truncated to 16 characters

## Examples

**Key Examples:**

- "Two nine" (8 chars) → "Two nine00000000" (16 chars)
- "mypassword" (10 chars) → "mypassword000000" (16 chars)  
- "thisisaverylongpassword" (22 chars) → "thisisaverylongp" (16 chars)

**Message Examples:**

- Short message: "Hello"
- Medium message: "This is a longer message that spans multiple blocks"
- Long message: "This is a very long message that demonstrates the capability of handling arbitrary length inputs in our AES implementation..."

## Important Notes

- **BOTH client and server must use the SAME key** for successful encryption/decryption
- The key adjustment happens automatically on both sides, so enter the same original key on both client and server
- Example: If you enter "Two nine" on client, enter "Two nine" (not "Two nine00000000") on server
