import os

os.system('pip install pyinstaller')
os.system('pyinstaller -F -w main.py')
print('\n*** ATTENTION ***\n')
print('There is only one step left:')
print('------------------------------------------------------------------------------------------------------------------------')
print('Move the "main.exe" generated in .\dist dirctory to "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"')
print('------------------------------------------------------------------------------------------------------------------------\n')
os.system('pause')