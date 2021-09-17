from sys import platform
import os

if platform == "linux" or platform == "linux2":
	os.system("apt install python3-pip")
	os.system("pip uninstall pycrypto")
	os.system("pip install -U PyCryptodome")
	os.system("sudo pip install bcrypt")
	print("Dependencies are installed.. Please run whitehorse.py to encrypt or decrypt the files.")
if platform == "darwin":
	os.system("curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python")
	os.system("sudo easy_install pip")
	os.system("pip uninstall pycrypto")
	os.system("pip install -U PyCryptodome")
	os.system("sudo pip install bcrypt")
	print("Dependencies are installed.. Please run whitehorse.py to encrypt or decrypt the files.")
if platform == "win32":
	os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
	os.system("python get-pip.py")
	os.system("pip uninstall pycrypto")
	os.system("pip install -U PyCryptodome")
	os.system("sudo pip install bcrypt")
	print("Dependencies are installed.. Please run whitehorse.py to encrypt or decrypt the files.")