import os
from os import path

def fileName(str, type):
    res = str.split(type)
    return res[1]

def lookSeed(file):
    string1 = ':Monkey:'
  
    # opening a text file
    file1 = open(file, "r")
    
    # setting flag and index to 0
    flag = 0
    
    # Loop through the file line by line
    for line in file1:          
        # checking string is present in line or not
        if string1 in line:
            flag = 1
            return fileName(fileName(line, " "), "=")
            
    # checking condition for string found or not
    if flag == 0: 
        print('String', string1 , 'Not Found') 
    
    # closing text file    
    file1.close() 

def monkeyCommand(package):
    #run the Monkey command on emulator
    file = fileName(package, ".") + "Monkey.txt"
    file2 = fileName(package, ".") + "Monkey2.txt"
    if path.exists(file):
        os.system("/usr/bin/time -a -o " + file2 + " -f '%E [elasped time] %M [maximum resident set size]' adb shell monkey -p " + package + " -s " + lookSeed(file) + " -v 200 > " + file2)
    else:
        os.system("/usr/bin/time -a -o " + file + " -f '%E [elasped time] %M [maximum resident set size]' adb shell monkey -p " + package + " -v 200 > " + file)
        


if __name__ == "__main__":
    val = input("Enter your file: ")
    monkeyCommand(val)