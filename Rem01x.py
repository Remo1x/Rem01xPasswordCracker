import hashlib
from hashing1 import hashtext
from readwordlist import readwl

print('''
============================================================================================
|                                                                                          |
|    $$$$$$$$$$$$$$    $$$$$$$$$$         $       $         $$$$$$$$$      $     $       $ |           
|    $            $    $                 $ $     $ $        $       $    $ $      $     $  |    
|    $            $    $                $   $   $   $       $       $   $  $       $   $   |   
|    $$$$$$$$$$$$$$    $               $     $ $     $      $       $  $   $        $ $    |                          
|    $ $               $$$$$$$$$$     $       $       $     $       $      $         $     |
|    $   $             $             $                 $    $       $      $        $ $    |
|    $     $           $            $                   $   $       $      $       $   $   |
|    $       $         $           $                     $  $       $      $      $     $  |
|    $         $       $$$$$$$$$$ $                       $ $$$$$$$$$  $$$$$$$$$ $       $ |
|                                                                                          |              
| Author: Rem01x                                                                           |
| Tool: Rem01x Password Cracker                                                            |
| Version: 1.0                                                                             |
============================================================================================''')

print("Please Enter A Hash To Decrypt: ")

hash = input()

print("Please Enter The Hash Type Needed For The Attack: ")

hashtype = input()

print("Please Enter Wordlist For Dectinary Attack: ")
wordlist = input()

rwl = readwl()

readwordlist = rwl.readwordlist(wordlist)

hashing = hashtext()

for i in readwordlist:
    i = i.strip("\n")
    hasht = hashing.hashingtext(i,hashtype)
    if hash == hasht :
        break

if hash == hasht :
        print("State: Cracked")
        print("Hash Entered: " + hash)
        print("Used Hash Type: " + hashtype)
        print("Password Is: " + i)

        
else :
    print("State: Not Cracked")
    print("Hash Entered: " + hash)
    print("Used Hash Type: " + hashtype)
    print("Password Not Found :(")