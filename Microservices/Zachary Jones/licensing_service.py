iimport random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

class LicensingService:
    def __init__(self, license_store='licenses.txt'):
        self.license_store = license_store

    def generate_license_key(self):
        """Generate a unique license key."""
        new_license_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        self.store_license_key(new_license_key)
        return new_license_key

    def store_license_key(self, key):
        """Store the generated license key in a file."""
        with open(self.license_store, 'a') as file:
            file.write(key + '\n')

    def _read_license_keys(self):
        """Read all license keys from the file."""
        try:
            with open(self.license_store, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

    def verify_license_key(self, key):
        """Verify if the license key is valid."""
        valid_keys = self._read_license_keys()
        return key in valid_keys

service = LicensingService()

@app.route('/generate', methods=['GET'])
def generate_key():
    new_key = service.generate_license_key()
    return jsonify({'license_key': new_key})

@app.route('/verify', methods=['POST'])
def verify_key():
    data = request.json
    key_to_verify = data.get('license_key')
    is_valid = service.verify_license_key(key_to_verify)
    return jsonify({'valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)

