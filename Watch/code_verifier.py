import secrets
import hashlib
import base64

# Generate a random code_verifier between 43 and 128 characters
code_verifier = secrets.token_urlsafe(43)[:128]

# Use the code_verifier in your request


# Assuming code_verifier is generated as above
code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode()).digest()).decode().rstrip('=')
print(code_verifier)
print(code_challenge)


