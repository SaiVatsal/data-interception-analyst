import base64

print("Scanning document for steganographic anomalies...")

# Open the infected file and read the raw text
with open("classified_memo.txt", "r", encoding="utf-8") as file:
    infected_text = file.read()

# -------------------------------------------------------------------------
# TODO 1: EXTRACT THE BINARY
# Create an empty string named 'extracted_binary'.
# Loop through every character in 'infected_text'.
# -------------------------------------------------------------------------

extracted_binary = ""

# Write your extraction loop here...
for char in infected_text:
    if char == '\u200b':    # Zero-Width Space
        extracted_binary += "0"
    elif char == '\u200c':  # Zero-Width Non-Joiner
        extracted_binary += "1"

if len(extracted_binary) > 0:
    print("Hidden binary payload detected!")
else:
    print("No hidden data found.")

# -------------------------------------------------------------------------
# TODO 2: DECODE THE ASCII
# Computers read characters in 8-bit chunks (bytes).
# Loop through 'extracted_binary' in steps of 8.
# For each 8-character chunk:
# 1. Convert the binary string to an integer: int(chunk, 2)
# 2. Convert the integer to a character: chr()
# 3. Append the character to the resulting string
# -------------------------------------------------------------------------

decoded_ascii = ""

# Write your ASCII decoding loop here...
for i in range(0, len(extracted_binary), 8):
    chunk = extracted_binary[i:i+8]
    # Ensure we only process full 8-bit chunks
    if len(chunk) == 8:
        chunk_int = int(chunk, 2)
        decoded_ascii += chr(chunk_int)

print("First layer cracked. Payload is Base64 encoded.")

# -------------------------------------------------------------------------
# TODO 3: THE BASE64 DOUBLE-WRAP
# - The 'decoded_ascii' string you just built is not the final flag.
# - It is a Base64 encoded string. You must decode it to reveal the truth.
# -------------------------------------------------------------------------

final_flag = ""

# Write your Base64 decoding step here...
# base64.b64decode returns bytes, so we must decode it back into a standard utf-8 string
decoded_bytes = base64.b64decode(decoded_ascii)
final_flag = decoded_bytes.decode('utf-8')

# Final result
print("--- DECODED FLAG ---")
print(final_flag)
print("--------------------")