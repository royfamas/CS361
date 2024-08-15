Communication Contract:

Endpoints

- Generate License Key
  URL: /generate
  Method: GET
  Description: Generates a new unique license key and stores it in a file.

- Verify License Key
  URL: /verify
  Method: POST
  Description: Verifies if a given license key is valid.

1. Request Data (Generating a license key)
- Make sure licensing_service.py is running by using "python licensing_service.py"
- use the command "curl http://127.0.0.1:5000/generate" to generate a key
- Alternatively, you can run the test file "test_licensing_service.py" to generate a key, verify it, and test for an invalid key. (this process creates licenses.txt with the random generated key included)


2. Recieve Data (Verify the generated key)
- make sure licenses.txt exists by running the program and generating a key
- use "curl -X POST -H "Content-Type: application/json" -d '{"license_key": "YOUR_LICENSE_KEY_HERE"}' http://127.0.0.1:5000/verify"
  to verify if a key exist. (replace 'YOUR_LICENSE_KEY_HERE' with the key you want to test)
  for example, if the generated key was "random112233" use "curl -X POST -H "Content-Type: application/json" -d '{"license_key": "random112233"}' http://127.0.0.1:5000/verify"
  to verify if they exist, this should return true if it does or false if it doesn't.

3. UML Diagram:
   Can be found in the directory as uml.PNG

4.
a) For which teammate did you implement “Microservice A”?
Zachary Jones

b) What is the current status of the microservice? 
It's done.

c) If the microservice isn’t done, which parts aren’t done and when will they be done?
It's done.

d) How is your teammate going to access your microservice? Should they get your code from GitHub? Should they run your code locally? Is your microservice hosted somewhere? Etc.
Github.

e) If your teammate cannot access/call YOUR microservice, what should they do? Can you be available to help them? What’s your availability?
They can reach out to me in discord and I'll get back to them when I can.

f) If your teammate cannot access/call your microservice, by when do they need to tell you?
Whenever they have an issue with the microservice.

g) Is there anything else your teammate needs to know? Anything you’re worried about? Any assumptions you’re making? Any other mitigations / backup plans you want to mention or want to discuss with your teammate?
I'm worried that my teammate wants this microservice done in a specific way that is different from the one I made which means I either have to remake the microservice or he has to create a main program that utilizes my format, Both cases being not ideal.


Code Improvements
Refactored verify_license_key Method
In the revised version, the verify_license_key method has been refactored for improved efficiency and readability. Previously, the method performed file reading and key verification in one step. Now, file reading has been separated into a private method _read_license_keys, which reads all license keys from the file. This change reduces complexity and improves performance.

Improved Variable Naming
Variable names have been updated for better clarity. For instance, key in the generate_license_key method has been renamed to new_license_key to better reflect its purpose.

