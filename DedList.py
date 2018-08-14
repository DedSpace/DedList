# -*- coding: utf-8 -*-
"""
Created on Fri Aug 03 01:23:25 2018

@author: DedSpace
"""
import itertools as it
import optparse as opt

logo = """
    _______              _____               _  
    \      \            | \   \    ___   ___| |___ 
    |      | _____  ____| |   |   |__/ __\__   __/ 
    |   |  |/  _  \/      |   |__/|  |/  __/| |  
    |      |    __/|  |   |       |  |__   || |  
   /_______/\_____/\____|_/\______|__/_____/\_/ 
                              
     Password Generator by DedSpace
    
     BTC Address: 3HMFX9SApf6F7eFvbWEEEqSa7cpGKrFQjY

   ---------------------------------------------------\n"""

use = "  Usage: \"-h\" or \"--help\" for usage.\n"

def compilelist(chars, length, name, duplicates):
    if duplicates>length:
        duplicates = length
    if duplicates == None:
        duplicates = 2
    n, m = 0, 0
    if type(name) == str:
        ttlist = open(name+str(n)+".txt", 'w')
    ref = []
    if name:
        print logo
        print use
        print "[+] Compiling list, please be patient...\n"
    for i in range(length):
        ref.append(0)
    for i in it.product(chars,repeat=length):
        check = []
        for j in i:
            if i.count(j) < duplicates+1:
                check.append(0)
            else:
                check.append(1)
        if check == ref:
            if type(name) == str:
                ttlist.write(''.join(i)+"\n")
                n += 1
                if n > 50000000:
                    m += 1
                    ttlist.close()
                    n = 0
                    ttlist = open(name+str(m)+".txt", 'w')
            else:
                print ''.join(i)
    if type(name) == str:
        ttlist.close()
        print "[+] Done, happy cracking!\n"

def main():
    usage="dedlist -c <characters> -l <pass length> -f <filename>"
    parser = opt.OptionParser(usage)
    parser.add_option("-c", dest="chars",      type="string", help="Character list to be used e.g. abc123")
    parser.add_option("-l", dest="length",     type="int", help="Desired length of password")
    parser.add_option("-f", dest="name",       type="string", help="Filename to save passwords (leave blank to pipe)\
                                                 \n                 WANRING, THIS WILL CAUSE THE PASSWORDS TO BE PRINTED!")
    parser.add_option("-d", dest="duplicates", type="int", help="Desired number of duplicate characters (default=2)")
    (options,args)=parser.parse_args()
    chars      = options.chars
    length     = options.length
    name       = options.name
    duplicates = options.duplicates
    if (chars == None) | (length == None):
        print logo
        print use
        print "  Psst... Characters and password length need to be set!\n"
        exit(0)
    compilelist(chars, length, name, duplicates)

if __name__=="__main__":
    main()
