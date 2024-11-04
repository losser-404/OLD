import os, platform, time, sys
os.system('clear')
print('\033[1;97m [💸] Checking For Update...')
os.system('git pull')
os.system('clear')
bit = platform.architecture()[0]
if bit == '64bit':
   print('\033[1;97m [✓] Found 64 Bit Device')
   import try
elif bit == '32bit':
   print('\033[1;97m [✓] Found 32 Bit Device')
   exit('\033[1;91m [×] Sorry Brother 32 Bit Device Not Supported')