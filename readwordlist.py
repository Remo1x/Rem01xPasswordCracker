import hashlib
class readwl :
    def readwordlist(self,wordlist) :
        rwl = open(wordlist,"r")
        return rwl.readlines()