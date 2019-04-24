from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from hashlib import sha256
import os
import bcrypt

def create_decrypt_name(filename):
	l = len(filename)
	temp = filename[::-1]
	tl = temp.index("/")
	return filename[0:(l-tl)]+"decrypted_"+filename[(l-tl):len(filename)]

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
	decrypt(path, passwrd)

def decrypt(filename,Key):
	blocksize = 64*1024

	print("*************************************************")
	print(filename + "  ==> path")
	outputFile = create_decrypt_name(filename)
	print(outputFile + "  ==> output path")
	Key = get_key(Key)

	with open(filename,'rb') as infile:
		size  = infile.read(16) # first 16 bytes length of file size
		filesize = size.decode()
		IV = infile.read(16)
		decryptor = AES.new(Key, AES.MODE_CBC, IV)
		with open(outputFile,'wb') as outfile:
			while True:
				block = infile.read(blocksize)
				if(len(block) == 0):
					break
				outfile.write(decryptor.decrypt(block))
			outfile.truncate(int(filesize))
if __name__ == '__main__':
	main()