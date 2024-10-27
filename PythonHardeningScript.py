import subprocess
'''
Python Script For Cyber Patriots Made By Basu Khadka


This Script Will Be Able To Do The Follwing Things

[1]. User Auditing
        [a]. Find Users that need to be added or removed
        [b]. Find Users Who Need Admin Privelage 
        [c]. Find Users Who Need Admin Privelage Removed
[2]. Disable Root Login From SSHD
[3]. Find And Remove Some Listed Hacking Services
[4]. Find And Remove Unauthorized Media Files 

'''

# User Auditing  

#Getting List of all authorized users
authorizedUsers = input('Enter List Of Authorized Users (Seperate names with comma and no spaces, eg: alex,bob,carl): ')
authorizedUsers = authorizedUsers.split(',')

#Getting List Of All Users On System
AllUsers = subprocess.run('ls /home', shell=True, capture_output=True, text=True)
AllUsers = AllUsers.stdout
AllUsers = AllUsers.split('\n')
AllUsers.pop(AllUsers.index(''))

#Making Them Both a Set
authorizedUsers = set(authorizedUsers)
AllUsers = set(AllUsers)

#Finding The Difference Between The Sets
UsersToBeDeleted = AllUsers - authorizedUsers
UsersToBeAdded = authorizedUsers - AllUsers
print(UsersToBeAdded)
print(UsersToBeDeleted)
number=0
if UsersToBeDeleted:
    print('\033[31;1mThe Following Users Are To Be Deleted!\033[1m')
    for i in UsersToBeDeleted:
        number+=1
        print(f'\033[0;31m    [{number}]. {i}\033[0m')
    for i in UsersToBeDeleted:
        greenlight = input(f'\033[1;4;31mDo You Want To Delete User {i} (y/n):\033[0m')
        greenlight.lower()
        if(greenlight == 'y'):
            command = f"sudo deluser {i} --remove-home"
            deleteCommand = subprocess.run(command,shell=True)
            if deleteCommand.returncode == 0:
                print(f'\033[32;1mUser {i} Was Deleted Succesfully!\033[0m')
else:
    print('\033[32;1mNo Users Are To Be Deleted!\033[0m')

if UsersToBeAdded:
    number=0
    print('\033[31;1;4mThe Following Users Are To Be Added!\033[0m')
    for i in UsersToBeAdded:
        number+=1
        print(f"\033[0;32m    [{number}]. {i}\033[0m")
    for i in UsersToBeAdded:
        greenlight = input(f'\033[1;4;31mDo You Want To Add User {i} (y/n):\033[0m')
        greenlight.lower()
        if(greenlight == 'y'):
            command = f"sudo adduser {i}"
            deleteCommand = subprocess.run(command,shell=True)
            if deleteCommand.returncode == 0:
                print(f'\033[32;1mUser {i} Was added Succesfully!\033[0m')
# End User Auditing