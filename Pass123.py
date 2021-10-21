import random, os, time, signal
from cryptography.fernet import Fernet
from colorama import Fore

#Locate the symmetric key, store its location in a file, save the contents as a variable, and delete the file
os.system("where /r c:\\users filekey.key > whereiskey.txt")
f = open("whereiskey.txt", "r")
keylocation = f.read().strip("\n")
f.close()
os.system("del whereiskey.txt")

#Decryption function to decrypt the password file using the symmetric key
def decrypt():
    os.system("attrib -h password.txt")
    with open(keylocation, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('password.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('password.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
    os.system("attrib +h password.txt")

#Decryption function to decrypt the defaultpass (master password) file using the symmetric key 
def decrypt_masterpass():
    os.system("attrib -h defaultpass.txt")
    with open(keylocation, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('defaultpass.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('defaultpass.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
    os.system("attrib +h defaultpass.txt")
 
#Encryption function to encrypt the password file using the symmetric key
def encrypt():
    os.system("attrib -h password.txt")
    with open(keylocation, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('password.txt', 'rb') as file:
        plaintext = file.read()
    encrypted = fernet.encrypt(plaintext)
    with open('password.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.system("attrib +h password.txt")

#Encryption function to encrypt the defaultpass (master password) file using the symmetric key
def encrypt_masterpass():
    os.system("attrib -h defaultpass.txt")
    with open(keylocation, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('defaultpass.txt', 'rb') as file:
        plaintext = file.read()
    encrypted = fernet.encrypt(plaintext)
    with open('defaultpass.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.system("attrib +h defaultpass.txt")
 
#Password generator function to take user input and generate a strong password using randomization
def passwordgenerator():
    password_generated_list = []
 
    #create a list of numbers 0 - 99 and randomly add one of the numbers to the generated password list
    number_list = []
    for num in range(0,100):
        number_list.append(num)
    random_number = random.choice(number_list)
    password_generated_list.append(str(random_number))
 
    #create a large list of categories to be used as questions for the user's generated password
    category_list = ["household item", "color", "computer brand", "country",'video game', 'sports team', 'city', 'food and drink', 'verb', 'adjective', 'profession', 'famous person', 'thing you find in the bathroom/kitchen', 'thing you take on holiday', 'fruit or vegetable', 'thing that flys', 'thing that is yellow', 'item you can buy in IKEA', 'thing you find inside your refrigerator', 'thing that is cold', 'thing you find in an office', 'thing that is round', 'thing that you find scary', 'thing related to Christmas', 'thing with wheels', 'thing in the garden', 'thing you can turn off', 'girls name', 'boys name', 'restaurant', 'ocean', 'reptile', 'piece of furniture', 'US state', 'National park', 'thing that you plug in', 'thing you do in the morning', 'thing you hang up', 'emotion', 'shiny object', 'thing that runs', 'thing that is fast', 'weather forecast', 'musical instrument', 'thing that is quiet', 'zoo animal', 'farm animal', 'hand tool', 'power tool', 'eating utensil', 'thing made of plastic', 'thing made of wood', 'thing made of paper', 'type of pet', 'thing you find in the bathroom', 'breakable object', 'thing with wheels', 'thing that rings', 'thing that is light', 'thing that is heavy', 'thing that opens', 'thing that locks', 'article of clothing', 'writing utensil', 'thing that is wet', 'hard object', 'dessert', 'furry animal', 'sharp thing', 'breakfast food', 'thing that is loud', 'thing with buttons', 'method of transportation', 'thing with numbers', 'thing that grows', 'container', 'item in a classroom', 'long object', 'small object', 'calendar month', 'holiday', 'marine animal', 'type of berry', 'retail store', 'fast food chain', 'type or meat', 'type of cheese', 'dairy product', 'thing that is blue','thing that is green', 'thing that is red','thing that is white','thing that is black', 'electronic device', 'type of fish', 'type of bird']
    random_word_1 = random.choice(category_list)
    random_word_2 = random.choice(category_list)

    #Ensure that all three questions do not use any of the same categories from the list
    while random_word_2 == random_word_1:
        random_word_2 = random.choice(category_list)
    random_word_3 = random.choice(category_list)
    while random_word_3 == random_word_1 or random_word_3 == random_word_2:
        random_word_3 = random.choice(category_list)

    #View the password file in order to compare its contents to user input
    os.system("attrib -h password.txt")
    f = open('password.txt', 'r')
    fstring = f.read()
    f.close()
    os.system("attrib +h password.txt")

    #Define the user's answer to question 1, ensure that it is longer than 3 characters, and has not been used previously
    ans_1 = input(Fore.LIGHTYELLOW_EX + '\nEnter a word related to a(n) ' + random_word_1 + ': ')
    if len(ans_1) <= 3:
        ans_1 = input(Fore.LIGHTRED_EX + '**ERROR**: must be longer than 3 characters: ' + Fore.LIGHTYELLOW_EX)
    while ans_1.upper() in fstring.upper():
        ans_1 = input(Fore.LIGHTRED_EX + '**ERROR**: This word has been previously used: ' + Fore.LIGHTYELLOW_EX)
    
    #Define the user's answer to question 2, ensure that it is longer than 3 characters, and has not been used previously
    ans_2 = input(Fore.LIGHTYELLOW_EX + 'Enter a word related to a(n) ' + random_word_2 + ': ')
    if len(ans_2) <= 3:
        ans_2 = input(Fore.LIGHTRED_EX + '**ERROR**: must be longer than 3 characters: ' + Fore.LIGHTYELLOW_EX)
    while ans_2.upper() in fstring.upper() or ans_2 == ans_1:
        ans_2 = input(Fore.LIGHTRED_EX + '**ERROR**: This word has been previously used: ' + Fore.LIGHTYELLOW_EX)
    
    #Define the user's answer to question 3, ensure that it is longer than 3 characters, and has not been used previously 
    ans_3 = input(Fore.LIGHTYELLOW_EX + 'Enter a word related to a(n) ' + random_word_3 + ': ')
    if len(ans_3) <= 3:
        ans_3 = input(Fore.LIGHTRED_EX + '**ERROR**: must be longer than 3 characters: ' + Fore.LIGHTYELLOW_EX)
    while ans_3.upper() in fstring.upper() or ans_3 == ans_2 or ans_3 == ans_1:
        ans_3 = input(Fore.LIGHTRED_EX + '**ERROR**: This word has been previously used: ' + Fore.LIGHTYELLOW_EX)
    
    #Create a list of lowercase letters
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string1 = ''
    string2 = ''
    string3 = ''
    wordlist = [ans_1, ans_2, ans_3]
 
    for items in wordlist:
        
        #Capitalize a random letter from answer 1 and add it to the generated password list
        if items == ans_1:
            random_letter = random.choice(alphabet)
            for char in ans_1:
                while random_letter not in ans_1:
                    random_letter = random.choice(alphabet)
                if char == random_letter:
                    char = char.upper()
                else:
                    char = char
                string1 += char
            password_generated_list.append(string1)
 
        #Capitalize a random letter from answer 2 and add it to the generated password list
        if items == ans_2:
            random_letter_2 = random.choice(alphabet)
            for char in ans_2:
                while random_letter_2 not in ans_2:
                    random_letter_2 = random.choice(alphabet)
                if char == random_letter_2:
                    char = char.upper()
                else:
                    char = char
                string2 += char
            password_generated_list.append(string2)

        #Capitalize a random letter from answer 3 and add it to the generate password list
        if items == ans_3:
            random_letter_3 = random.choice(alphabet)
            for char in ans_3:
                while random_letter_3 not in ans_3:
                    random_letter_3 = random.choice(alphabet)
                if char == random_letter_3:
                    char = char.upper()
                else:
                    char = char
                string3 += char
            password_generated_list.append(string3) 
 
    #Create a list of special characters/symbols that are generally accepted for most websites
    special_char_list = ['!','@','#','$','%','&','*','?','_','-']
    #Generate a random symbol from the list
    random_special = random.choice(special_char_list)
    #Generate a 2nd random symbol from the list
    random_special_2 = random.choice(special_char_list)
    #Ensure that the 2 symbols are not identical and add them to the generated password list
    while random_special_2 == random_special:
        random_special_2 = random.choice(special_char_list)
    password_generated_list.append(random_special)
    password_generated_list.append(random_special_2)
 
    #Define the user's username and website associated with the generated password
    username = input("\nWhat is your username: ")
    website = input("\nWhat website is this password for: ")
    
    #Randomize the order of the generated password list and create a string out of the elements of the list
    final_password = ''
    random.shuffle(password_generated_list)
    for items in password_generated_list:
        final_password += items
    #Format the user's new password, website, and username to be stored in the password file
    fileadd = Fore.RESET + "Website: " + Fore.BLUE + website + Fore.RESET + " | Username: " + Fore.RED + username + Fore.RESET + " | Password: " + Fore.CYAN + final_password + Fore.RESET + "\n"
    os.system("attrib -h password.txt")
    f = open("password.txt", "a")
    #Add the newly formatted information to the password file
    f.write(fileadd)
    f.close()
    os.system("attrib +h password.txt")
    #Display the generated password to the user
    print("\nYour generated password is: " + final_password + "\n")

#Test a user provided password for strength based on 6 quantifiable metrics 
def pass_strength():
    
    length_score = 0
    case_complexity_score = 0
    number_score = 0
    special_char_score = 0
    repeating_score = 0
    incrementing_score = 0
    
    #Define the user's provided password
    passwd = input(Fore.LIGHTYELLOW_EX + "\nWhat is your password?: ")
    #Define the length of the user's password
    length_of_password = len(passwd)
    #Calculate length score based on password length
    if length_of_password <= 6:
        length_score = 0
    elif length_of_password > 6 and length_of_password <=10:
        length_score = 18
    else:
        length_score = 30
    
    #Calculate case complexity score based on variation between upper and lowercase characters
    upper = False
    lower = False
    for char in passwd:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        else:
            break
    #If the password contains both upper and lowercase characters, give it a score of 12
    if upper == lower:
        case_complexity_score = 12
    #If the password contains all upper or all lowercase characters, give it a score of 5
    else:
        case_complexity_score = 5
 
    #Create a counter for the amount of numbers that the password contains, create number score based on the counter
    digit_counter = 0
    for char in passwd:
        if char.isdigit():
            digit_counter += 1
    if digit_counter == 0:
        number_score = 0
    elif digit_counter == 1:
        number_score = 5
    else:
        number_score = 7
 
    #Calculate special character score based on the passwords use of the symbols contained within the following string of symbols
    special_counter = 0
    for char in passwd:
        if char in "[@_!#$%&*?-":
            special_counter += 1
    if special_counter == 0:
        special_char_score = 0
    elif special_counter == 1:
        special_char_score = 7
    else:
        special_char_score = 10
 
    #Calculate repeating/identical character score using a counter
    charcount = 0
    singlecount = 1
    preceeding_char = None
    #As we go through the characters of the password, check to see if they match the previous character and add to the counter 
    for char in passwd:
        if char == preceeding_char:
            singlecount += 1
            charcount = max(charcount, singlecount)
        else:
            singlecount = 0
        preceeding_char = char
    if charcount == 0:
        repeating_score = 21
    if charcount == 1:
        repeating_score = 19
    if charcount == 2:
        repeating_score = 0
 
    #Calculate incrementing character score based on the most common alphabetical and numercial incrementations in the following list
    characters = ['abc','bcd','cde','123','234','345','456','567','678','789']
    for i in characters:
        if i in passwd:
            incrementing_score += 20
        else:
            incrementing_score +=0
    if incrementing_score > 0:
        incrementing_score = 0
    else:
        incrementing_score = 20
    
    #Calculate the total password score out of 100 by adding the 6 metrics together
    total_score = length_score + case_complexity_score + number_score + special_char_score + repeating_score + incrementing_score      
    #Create overriding rule to reduce password score based on password length  
    if length_score == 0:
        total_score -= 20
    if length_of_password < 4:
        total_score = 0
    #Display the total password score to the user
    print("\nYour password score is: " + (str(total_score) + '/100\n'))
 
#Function to change a user's store password
def change_pass():
    x = Fore.RED + "**No password is stored for this website**" + Fore.RESET
    #Define the website which the user would like to change the password for
    old_pass = input(Fore.LIGHTYELLOW_EX + "\nWhat website do you want to change your password for: ")
    os.system("attrib -h password.txt")
    oldfile = open("password.txt", "r")
    #Read through each line of the password file and check to see if that website has been stored previously
    lines = oldfile.readlines()
    for individual_line in lines:
        if old_pass.upper() in individual_line.upper():
            x = individual_line
    oldfile.close()
    os.system("attrib +h password.txt")
    #Display the website, username, and password information related to that website or tell the user that the website has not been stored previously
    print("\n" + x)

    if x != Fore.RED + "**No password is stored for this website**" + Fore.RESET:
        #If the website has had a previously stored password, define the new password and username 
        new_password = input(Fore.LIGHTYELLOW_EX + "What is your new password: ")
        username = input("\nWhat is your username: ")
        #Format the new password information
        fileadd = Fore.RESET + "Website: " + Fore.BLUE + old_pass + Fore.RESET + " | Username: " + Fore.RED + username + Fore.RESET + " | Password: " + Fore.CYAN + new_password + Fore.RESET + "\n"
        print(Fore.GREEN + "\nSuccessfully updated" + Fore.RESET)
        #Display the newly formatted information to the user
        print("\n" + fileadd)

        #Remove the previously stored password information
        os.system("attrib -h password.txt")
        newfile = open("password.txt", "w")
        for line in lines:
            if line != x:
                newfile.write(line)
        newfile.close()

        #Replace the removed password information with the newly changed information
        f = open("password.txt", "a")
        f.write(fileadd)
        f.close()
        os.system("attrib +h password.txt")

#Function to search for a stored password
def search_pass():
    x = Fore.RED + "**No password is stored for this website**" + Fore.RESET
    #Define the website which the user would like to change the password for
    old_pass = input(Fore.LIGHTYELLOW_EX + "\nWhat website do you want to search the password for: ")
    os.system("attrib -h password.txt")
    oldfile = open("password.txt", "r")
    lines = oldfile.readlines()
    #Search through the password file for the website provided by the user
    for individual_line in lines:
        if old_pass.upper() in individual_line.upper():
            x = individual_line
    oldfile.close()
    os.system("attrib +h password.txt")
    #Display the password information related to the searched website
    print(Fore.RESET + "\n" + x)

#Function to provide the user with a terminal menu as well as providing total feature functionality by calling the previously defined functions 
def main_app():
    #Try statement to wrap the proper use of the application
    try:
        #Wrap the entire running of the application in the requriement that the symmetric key be located on the computer
        if len(keylocation) > 0:
            os.system("attrib -h defaultpass.txt && attrib -h password.txt")
            f = open("defaultpass.txt", "r")
            y = f.read()
            f.close()
            f = open("password.txt", "r")
            x1 = f.read()
            f.close()
            os.system("attrib +h defaultpass.txt && attrib +h password.txt")
            #Upon first use, view the password and master password files to ensure that they have not been changed from their original state
            #____default____password____ ensures that the the master password has yet to be set
            #gAAAAABg not being within the password file ensures that it has yet to be encrypted, meaning the application has never been run
            if y == "____default____password____" and "gAAAAABg" not in x1:
                print(Fore.CYAN + "------- Welcome to Pass123, the All Inclusive Password Tool -------" + Fore.RESET)
                master_reset = 1
                while master_reset == 1:
                    #Prompt user to create a master password and double check their typing in order to confirm the master password
                    newpass = input(Fore.LIGHTYELLOW_EX + "\nWhat would you like to use as a master password: ")
                    confirm_newpass = input("\nConfirm your master password: ")
                    os.system("cls")
                    if newpass == confirm_newpass:
                        os.system("attrib -h defaultpass.txt")
                        newmaster = open("defaultpass.txt", "w")
                        newmaster.write(confirm_newpass)
                        newmaster.close()
                        os.system("attrib +h defaultpass.txt")
                        print(Fore.GREEN + "\nMaster Password Succefully Saved" + Fore.RESET)
                        master_reset = 0
                        time.sleep(3)
                        os.system("cls")

            #With each sequential use of the application, require the user to provide their stored master password
            masterpass = input(Fore.LIGHTCYAN_EX + "Enter your master password: ")
            os.system("cls")
            os.system("attrib -h defaultpass.txt")
            f = open("defaultpass.txt", "r")
            x = f.read()
            f.close()
            #Check to see if the master password provided is correct, and encrypt the defaultpass (master password) file if it is in clear text
            #This will only be the case after the user has created a master password but has yet to make it to the application's main terminal menu
            #The application requires that both password and master password files are encrypted upon its startup because it can't decrypt clear text
            if masterpass in x and "gAAAAABg" not in x1:
                with open(keylocation, 'rb') as filekey:
                    key = filekey.read()
                fernet = Fernet(key)
                with open('defaultpass.txt', 'rb') as file:
                    plaintext = file.read()
                encrypted = fernet.encrypt(plaintext)
                with open('defaultpass.txt', 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
            decrypt_masterpass()
            os.system("attrib -h defaultpass.txt")
            f = open("defaultpass.txt", "r")
            #Authenticate user by comparing the provided master password to the previously stored master password
            if masterpass == f.read():
                encrypt_masterpass()
                f.close()
                os.system("attrib +h defaultpass.txt")

                while True:
                    #Automatically encrypt the password file as a failsafe to account for improper manipulation or application malfunction 
                    os.system("type password.txt > encryptionTest.txt")
                    f = open("encryptionTest.txt", "r")
                    password_string = f.read()
                    f.close()
                    if "gAAAAAB" not in password_string:
                        encrypt()
                    os.system("del encryptionTest.txt")
                    #Display the main terminal window of the application with the program features
                    print(Fore.CYAN + "\n-----Password Menu-----\n")
                    print(Fore.YELLOW + "1.Test a Password")
                    print("2.Add a Password to Stored Passwords")
                    print("3.Generate New Password / Update Existing Password")
                    print("4.Search for a Stored Password") 
                    print("5.Change a Password")   
                    print("6.Exit\n" + Fore.RESET)
                    choice=input("Enter Option Number: ")
                    
                    #If the user chooses option 1, call the password strength function
                    if choice=="1":
                        pass_strength()
                        time.sleep(7)
                        os.system("cls")
        
                    #If the user chooses option 2, store their provided password, website, and username information
                    elif choice=="2":
                        own_passwd = input(Fore.LIGHTYELLOW_EX + "\nWhat password do you want to store: ")
                        username2 = input("\nWhat is your username: ") 
                        website2 = input("\nWhat website is this password for: ")
                        fileadd = Fore.RESET + "Website: " + Fore.BLUE + website2 + Fore.RESET + " | Username: " + Fore.RED + username2 + Fore.RESET + " | Password: " + Fore.CYAN + own_passwd + Fore.RESET + "\n"
                        os.system("attrib -h password.txt")
                        decrypt()
                        f = open("password.txt", "a")
                        f.write(fileadd)
                        f.close()
                        encrypt()
                        time.sleep(1)
                        os.system("cls && attrib +h password.txt")
        
                    #If the user chooses option 3, call the password generator function
                    elif choice=="3":
                        os.system("attrib -h password.txt")
                        decrypt()
                        passwordgenerator()
                        encrypt()
                        time.sleep(10)
                        os.system("cls && attrib +h password.txt")
                    
                    #If the user chooses option 4, call the password search function
                    elif choice=="4":
                        os.system("attrib -h password.txt")
                        decrypt()
                        search_pass()
                        time.sleep(10)
                        encrypt()
                        os.system("cls && attrib +h password.txt")
        
                    #If the user chooses option 5, call the password change function 
                    elif choice=="5":
                        os.system("attrib -h password.txt")
                        decrypt()
                        change_pass()
                        encrypt()
                        time.sleep(7)
                        os.system("cls && attrib +h password.txt")
                    
                    #If the user chooses option 6, exit out of the application 
                    elif choice=="6":
                        os.system("cls")
                        os.system("attrib +h password.txt && attrib +h defaultpass.txt")
                        break

                    #If the user chooses any other option other than 1-6, display an error message and provide the terminal window again
                    else:
                        print(Fore.LIGHTRED_EX + "\n**Invalid Option Number**")
                        time.sleep(3)
                        os.system("cls")
           
            #If the user provides an incorrect master password, exit out of the application
            else:
                encrypt_masterpass()  
                os.system("attrib +h password.txt && attrib +h defaultpass.txt")
    #Failsafe to ensure the encryption and rehiding of the password and defaultpassword (master password) files upon improper exit of application
    except EOFError:
        encrypt()
        os.system("attrib +h password.txt && attrib +h defaultpass.txt")
    #Failsafe to ensure the encryption and rehiding of the password and defaultpassword (master password) files upon keyboard interruption
    except KeyboardInterrupt:
        encrypt()  
        os.system("attrib +h password.txt && attrib +h defaultpass.txt")
main_app()
