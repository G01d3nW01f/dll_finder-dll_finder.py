#!/usr/bin/python3

import os
import sys
import urllib.request
import hashlib
import subprocess

def init():
    logo = """
    + + + + + + + + + + + + +

    + Emotet DLL Gathering  +

    + + + + + + + + + + + + +
    """
    print(logo)
    
    usage = f"""
    
    {sys.argv[0]} <file_name>
    """

    if len(sys.argv) != 2:
        print("[!]Need more argument")
        print(usage)
        sys.exit()

def file_read():
    
    file_4_read = sys.argv[1]

    f = open(file_4_read,"r")
    array = f.read()
    array = array.split('\n')
    f.close()
    return array

def file_download(array):

    file_name = "test.dll"
    hash_array = []
    for i in array:
        try:
            file = urllib.request.urlretrieve(i,"test.dll")
            file_hash = hashlib.md5(open(file_name,'rb').read()).hexdigest()
            os.system(f"mv test.dll {file_hash}.dll")
            print(f"{i} -> {file_hash}")
            hash_array.append(file_hash)

        except:
            print("[!]Exception Occured")
        #except KeyboardInterrupt:
         #   print("[-]KeyBoard Intterupt!!!!")
    
    return hash_array

def report_maker(hash_array):

    f = open("report.txt","w")
    for i in hash_array:
        f.write(i+"\n")
    f.close()

def main():
    init()
    array = file_read()
    hash_array = file_download(array)
    report_maker(hash_array)

if __name__ == "__main__":

    main()
