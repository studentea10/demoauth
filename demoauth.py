import pyotp
import time

def generate_secret_key():
    # Generate a random secret key
    return pyotp.random_base32()

def generate_otp(secret_key):
    # Create a TOTP object with the secret key
    totp = pyotp.TOTP(secret_key)
    # Generate the current OTP
    return totp.now()

def verify_otp(secret_key, user_input_otp):
    # Create a TOTP object with the secret key
    totp = pyotp.TOTP(secret_key)
    # Verify the entered OTP
    return totp.verify(user_input_otp)

# Example Usage:
if __name__ == "__main__":
    # Step 1: Generate a secret key for the user
    secret_key = generate_secret_key()
    print(f"Secret Key: {secret_key}")

    # Step 2: Display the QR code (optional, for mobile authenticator apps)
    totp = pyotp.TOTP(secret_key)
    print(f"Scan the following QR code in your authenticator app:\n{totp.provisioning_uri('your-username', issuer_name='YourApp')}")

    # Step 3: Simulate user login
    user_entered_otp = input("Enter the OTP from your authenticator app: ")

    # Step 4: Verify the entered OTP
    if verify_otp(secret_key, user_entered_otp):
        print("Authentication Successful!")
    else:
        print("Authentication Failed!")
