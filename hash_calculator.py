import hashlib

# Function to calculate the hash
def calculate_hash(algorithm, text):
    if algorithm == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(text.encode()).hexdigest()
    else:
        return None

# Get user input
user_input = input("Please enter the text: ")
algorithm = input("Please choose an algorithm (md5, sha256, sha1, sha512): ").lower()

# Calculate the hash based on the chosen algorithm
hash_result = calculate_hash(algorithm, user_input)

# Print the result
if hash_result:
    print(f"The {algorithm.upper()} hash of '{user_input}' is: {hash_result}")
else:
    print("Unsupported algorithm. Please choose md5, sha256, sha1, or sha512.")

