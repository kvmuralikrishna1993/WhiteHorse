Project White Horse.
====================

The **White Horse** is a tool designed to encrypt small files like text files, images, audio files etc. using **AES (Advanced Encryption Standard)**, a symmetric block algorithm. Further, it uses **Secure Hash Algorithms{SHA256}** and **bcrypt**, to generate the hash[digest] using password, which is used to encrypt the data.

--------------------------------------------------------------------------------------

**#OneWayEncrytion(SHA256 and bcrypt)**

**#Caution : If key is Lost, data will be Lost.**

--------------------------------------------------------------------------------------

## More about **_WhiteHorse_**:

==> Written in **_Python3_**.

==> **_White Horse_** will encrypt the data by taking **_path of the file_** and **_password_** as input.

==> The detail explanation of each line of code is written in comments.

==> Check the **_helper functions_** for more detials.

----------------------------------------------------------------------------------------

## **_for PIP_** [Ignore if pip exists]

$apt install python3-pip

## To run the tool please install the following packages using  **_pip_**:

**_[enter the password for permissionsto install dependency modules]_**

## **_for AES_**
$pip uninstall pycrypto
$pip install -U PyCryptodome

## **_for salting purpose_**
$sudo pip install bcrypt

