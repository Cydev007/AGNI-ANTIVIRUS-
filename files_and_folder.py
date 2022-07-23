import hashlib
import os

import json
# import agnihome as agh
from functools import partial

progress = 0
proceed = -1


def scan_sha256(file):
    global progress
    global proceed
    virus_found = False

    with open(file, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest();

        print("The SHA256 hash of this file is: " + readable_hash)

        with open("D:\\TNU\\4th Sem\\Python\\lab\\AGNI Total Security\\Hashes\\SHA256.txt", 'r') as f:
            lines = [line.rstrip() for line in f]
            for line in lines:
                if str(readable_hash) == str(line.split(";")[0]):
                    virus_found = True

            f.close()
            progress = 100

    if not virus_found:
        proceed = 2
        progress = 100




def scan_md5(file):
    global progress
    global proceed
    virus_found = False

    with open(file, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.md5(bytes).hexdigest();

        print("The MD5 hash of this file is: " + readable_hash)

        with open("D:\\TNU\\4th Sem\\Python\lab\\AGNI Total Security\\Hashes\\MD5 Virus Hashes.txt", 'r') as f:
            lines = [line.rstrip() for line in f]
            for line in lines:
                if str(readable_hash) == str(line.split(";")[0]):
                    virus_found = True

            f.close()
            progress = 50
    if not virus_found:
        proceed = 1
        progress = 50


def scan_sha1(file):
    global progress
    global proceed
    virus_found = False

    with open(file, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha1(bytes).hexdigest();

        print("The SHA1 hash of this file is: " + readable_hash)

        with open('D:\\TNU\\4th Sem\\Python\lab\\AGNI Total Security\\Hashes\\SHA1 HASHES.json', 'r') as f:
            dataset = json.loads(f.read())

            for index, item in enumerate(dataset["data"]):
                if str(item['hash']) == str(readable_hash):
                    virus_found = True

            f.close()

    if not virus_found:
        proceed = 0
        progress = 30


def scan(file):
    global proceed
    global progress
    scan_sha1(file)
    print(f"proceed = {proceed} progress = {progress}")
    if proceed == 0:
        scan_md5(file)
        print(f"proceed = {proceed} progress = {progress}")
        if proceed == 1:
            scan_sha256(file)
            print(f"proceed = {proceed} progress = {progress}")
            if proceed == 2:
                print('File is safe')
            else:
                print('FIle is Unsafe')
        else:
            print('FIle is Unsafe')
    else:
        print('FIle is Unsafe')

