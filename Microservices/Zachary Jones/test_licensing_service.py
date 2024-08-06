import requests

def test_generate_and_verify():
    base_url = 'http://127.0.0.1:5000'

    # Generate a key
    response = requests.get(f'{base_url}/generate')
    data = response.json()
    new_key = data.get('license_key')

    print(f"Generated License Key: {new_key}")

    # Verify the newly generated license key
    response = requests.post(f'{base_url}/verify', json={'license_key': new_key})
    data = response.json()
    is_valid = data.get('valid')

    print(f"License Key {new_key} is valid: {is_valid}")

    # Test with an invalid key
    invalid_key = 'BADKEY111111'
    response = requests.post(f'{base_url}/verify', json={'license_key': invalid_key})
    data = response.json()
    is_valid = data.get('valid')

    print(f"License Key {invalid_key} is valid: {is_valid}")

if __name__ == '__main__':
    test_generate_and_verify()
