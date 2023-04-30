import secrets, string, hashlib

# Choose a hash algorithm
# You can choose from: 'sha256', 'blake2s', 'shake_256', 'sha3_512', 'sha1', 'sha3_384', 'shake_128', 'sha3_224', 'sha3_256', 'md5', 'blake2b', 'sha512', 'sha224', 'sha384'
hash_algorithm = "sha3_512"

# Define the characters to use for the password
password_characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random salt and password
salt, password = secrets.token_bytes(16), ''.join(secrets.choice(password_characters) for i in range(16)).encode()

# Hash the password using the chosen algorithm
hash_str = hashlib.new(hash_algorithm, salt + password).hexdigest()

# Print the results
print(f"Password: {password.decode()}")
print(f"Salt: {salt.hex()}")
print(f"Hash: {hash_str}")