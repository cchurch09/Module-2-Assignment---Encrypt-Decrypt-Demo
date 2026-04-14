
users = {"admin":{"password": "pass123", "role": "admin"}}

#User login information
username = "admin"
password = "pass123"

#Veify user and obtaining the role
if username in users and users[username]["password"] == password:
    role = users[username]["role"]
    print("Login Successful!")
    print("Role:", role)
else:
    print("Login Failed!")


#Encription Portion (Maybe go over with tutor)
message = "Hello"
sym_key = "key"  #future keys are gonna be different


#Encryption and Decryption portion def need to look into studying more
encrypted = ''.join(chr(ord(message[i]) ^ ord(sym_key[i % len(sym_key)]))
                    for i in range(len(message)))
decrypted = ''.join(chr(ord(encrypted[i]) ^ ord(sym_key[i % len(sym_key)]))
                    for i in range(len(encrypted)))


#Keys
public_key = (17, 3233)
private_key = (2753, 3233)

rsa_input = 65
rsa_encrypted = pow(rsa_input, public_key[0], public_key[1])
rsa_decrypted = pow(rsa_encrypted, private_key[0], private_key[1])


#Little confused on outputs ask tutor more information
print("Keys Used:")
print("Symmetric Key:", sym_key)
print("Public Key:", public_key)
print("Private Key:", private_key)

print("Inputs:")
print("Message:", message)
print("RSA Input:", rsa_input)

print("Outputs:")
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
print("RSA Encrypted:", rsa_encrypted)
print("RSA Decrypted:", rsa_decrypted)



#Ran into alot of problems with the encryption portions. Would not come with 
#correct output. Going to W3 schools and along with youtube videos had helped on figuring out. The tutor had also gone over key componets that I may have missed.

