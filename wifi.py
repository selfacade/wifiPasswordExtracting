
# lets first import the subprocess module this module is used to interact with cmd of windows
import subprocess

# Extracting profiles from window's using window's commands
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# profiles 
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# looping all the profiles networks
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b] # extracting passwords and filtering it in a format

    # now finally we will print the profiles and its passwords using try and except
    try:
        print(" {:<30}| {:<}".format(i, results[0]))
    except:
        print(" {:<30}| {:<}".format(i, ""))
input("")

