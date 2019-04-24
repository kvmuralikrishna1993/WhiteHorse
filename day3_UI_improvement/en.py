from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from hashlib import sha256
import os
import bcrypt

def create_encrypt_name(filename):
	l = len(filename)
	temp = filename[::-1]
	tl = temp.index("/")
	return filename[0:(l-tl)]+"encrypted_"+filename[(l-tl):len(filename)]

def get_key(Key):
	salt = b'$2b$12$221eTzU0zweNKfeX58oBcO' # generated random salt using bycrpt
	Key = bcrypt.hashpw(Key.encode('utf-8'), salt) #created a hash using bcrypt
	print(Key ,"  ==> salted Key")
	Key = sha256(Key).digest()[:16] #reduced to 16
	print(Key ,"  ==> encrypted Key")
	print("******************************************************")
	return Key

def main():
	path  = input("Enter path:  ")
	passwrd = input("Enter passwrd:  ")
	encrypt(path, passwrd)

def encrypt(filename, Key):
	blocksize = 64*1024

	print("*************************************************")
	print(filename + "  ==> path")
	outputFile = create_encrypt_name(filename)
	print(outputFile + "  ==> output path")

	filesize = str(os.path.getsize(filename)).zfill(16)
	print(filesize + "  ==> filesize in bytes")

	Key = get_key(Key)

	IV = Random.new().read(16)
	encryptor = AES.new(Key,AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile: #writing output file as binary
			outfile.write(filesize.encode('utf-8')) #encoding filesize utf -8
			outfile.write(IV) #writing intialised vector
			while True:
				block = infile.read(blocksize) # reading each block
				if len(block) == 0: #all blocks completed we stop operation
					break
				elif len(block) % 16 != 0: # if block is not equal to 16 bytes then we add padding so that it will be 16 by 
					block += b'}' * (16 - (len(block) % 16)) #16- 15%16 ==> 1
				outfile.write(encryptor.encrypt(block)) # encrypt and write the file.

if __name__ == '__main__':
	main()