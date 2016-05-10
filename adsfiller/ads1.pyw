import os, subprocess
import string, random
from ctypes import *
import shlex

        
#prevent searching for ADS files
def generate_secretfile(length=8, letters=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(letters) for digit in range(length))


wantedpath = 'C:/Users/Matt/Downloads/Nonsense'
dirs = []

for (dirpath,dirnames,filenames) in os.walk(wantedpath):
	dirs.extend(filenames)
	dirs.extend(dirnames)
	break

dirs.sort()
#print dirs

####adding ADS to each file using the following file
count=0
runs = 50 #10 = about 28kb; 100 = 45kb; 50 = 7.5mb -> 300mb with jpgs
while count < runs: 
        for i in range(len(dirs)-1):        
                secret = str(generate_secretfile(random.randint(5,22)))+'.txt' 
                #secret = "secret.txt"
                firstone = wantedpath+'/'+dirs[i]
                secondone = wantedpath+'/'+dirs[i+1]
                command = "(sort < %s) >> %s:%s" %(firstone,secondone,secret)
                args = shlex.split(command)
                subprocess.Popen(args, shell=True)
        count+=1



"""
libc = cdll.msvcrt
kernel = windll.kernel32

#testing generate_secretfile
i=0
for i in range(10):
        blue = generate_secretfile()
        yellow = generate_secretfile(20)
        print blue
        print yellow
        i +=1

a = generate_secretfile(random.randint(5,22))
print a
b = generate_secretfile()
print b
"""

"""
#type command wasn't working.
count = 0
while count<10:
        for i in range(len(dirs)-1):
                #secret = str(generate_secretfile(random.randint(5,22)))+'.txt' 
                secret = "secret.txt"
                arg1 = '"'+wantedpath+'/'+dirs[i]+'"'
                arg2 = '"'+wantedpath+'/'+dirs[i+1]+'"'
                print "arg1: " + arg1
                os.popen( "type %s > %s:%s" % (arg1,arg2,secret))
                print dirs[i+1]+':'+secret

        count +=1
"""

        
"""
#append to ADS
command = "echo hello & echo words.txt"
#run command
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

print process.communicate()[0].strip()

"""
