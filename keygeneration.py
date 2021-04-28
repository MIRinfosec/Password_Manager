from cryptography.fernet import Fernet

#Generate a symmetric key and give it a filename "filekey.key"
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
