# AGNI-ANTIVIRUS
## Developed by Cydev007 & Psbcg433
*************************************************************************************************************************************************************
## i. Malicious File Detection 
Malicious File Detection script is signature based.  This Tool written in python3  to determine virus, payloads and malicious files.  We create a database that contains MD5, SHA256 and SHA1 hashes of virus files ( Source: https://virusshare.com/ ).  Our tool detects if a scanned file is malicious or not.  Before diving into deeper, let’s just first understand what is Hashing, and the various hashing functions we have used in this project.

What is Hashing and Hash function?

Hashing is the process of transforming any given key or a string of characters into a fixed-length value using a hash function. A hash function is any function that can be used to map data of arbitrary size to fixed-size values.

Let us briefly see two popular hash functions –

#### Message Digest (MD)
The MD family comprises of hash functions MD2, MD4, MD5 and MD6. It is a 128-bit hash function.
MD5 digests have been widely used in the software world to provide assurance about integrity of transferred file.

#### Secure Hash Function (SHA)
Family of SHA comprise of four SHA algorithms: SHA-0, SHA-1, SHA-2, and SHA-3. Though from same family, there are structurally different.
The original version is SHA-0, a 160-bit hash function, was published by the National Institute of Standards and Technology (NIST) in 1993.
SHA-1 is the most widely used of the existing SHA hash functions. It is employed in several widely used applications and protocols.

SHA-2 family has four further SHA variants, SHA-224, SHA-256, SHA-384, and SHA-512 depending up on number of bits in their hash value. No successful attacks have yet been reported on SHA-2 hash function.
In October 2012, the NIST chose the Keccak algorithm as the new SHA-3 standard.

#### In this project we have used 3 major hashing functions; MD5, SHA-1, SHA-256.

### How The Script Works
![image](https://user-images.githubusercontent.com/108612723/177182720-bd355dc9-e474-4579-bc4b-711bfdf13c26.png)


When the script is executed, the functions open the file in binary mode and stores the binary value of the selected file into a variable. Then the desired hash value is generated using the variable storing the binary value of the original file with predefined hashlib function and stored into a different variable.
After completing up till this, then the stored hash value is checked with the available database of hash values. If the generated hash value is found and matched with the available hash values in the database, then the file is declared as a virus, and it prompts a warning and being quarantined or deleted by the OS. Or else, if the generated hash value is not found and matched with the available hash values in the database, then the file is declared as safe.


### ************************************************ *File Scaning* ***********************************************
*******************************************************************************************************************
![image](https://user-images.githubusercontent.com/108612723/178465722-9c620f9c-951c-401b-a720-130094d88d6a.png)


### <<Behind the scene
![image](https://user-images.githubusercontent.com/108612723/178467293-7d722004-67b5-46a1-b83d-dd7a358ca008.png)

![image](https://user-images.githubusercontent.com/108612723/178468036-31ea1d43-3ef3-474d-bc40-3579b00bd1d9.png)

### ********************************************** *Folder Scaning* ***********************************************
*******************************************************************************************************************
![image](https://user-images.githubusercontent.com/108612723/178468425-56db0f75-17c1-4974-a4d9-8e3fb62fe35f.png)
             
### <<Behind the scene
![Screenshot (118)](https://user-images.githubusercontent.com/108612723/178468817-bfe869ee-1944-4473-bb54-798a9f02353b.png)


The file is being checked with all the three hashing functions (i.e., MD5, SHA-1, SHA-256). If any one of the hashing functions declares the scanned file as virus, then overall the file is declared as a virus rather being declared safe by the other hashing functions and the next step is being initiated by the OS own by own. Same as that, if and only if the scanned file is declared safe by all the three hashing functions, then only the original file overall is declared safe and secure.



