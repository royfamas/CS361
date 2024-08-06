import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

class LicensingService:
    def __init__(self, license_store='licenses.txt'):
        self.license_store = license_store

    def generate_license_key(self):
        """Generate a unique license key."""
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        self.store_license_key(key)
        return key

    def store_license_key(self, key):
        """Store the generated license key in a file."""
        with open(self.license_store, 'a') as file:
            file.write(key + '\n')

    def verify_license_key(self, key):
        """Verify if the license key is valid."""
        try:
            with open(self.license_store, 'r') as file:
                valid_keys = file.read().splitlines()
            return key in valid_keys
        except FileNotFoundError:
            return False

service = LicensingService()

@app.route('/generate', methods=['GET'])
def generate_key():
    key = service.generate_license_key()
    return jsonify({'license_key': key})

@app.route('/verify', methods=['POST'])
def verify_key():
    data = request.json
    key = data.get('license_key')
    is_valid = service.verify_license_key(key)
    return jsonify({'valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)
