# importing the csv module
import csv
from xmlrpc.client import Boolean


def email_id_check(em):#validates the input mail ID, Returns Boolean.
    if "@" and "." in em:
        pass
        if em.index("@") < em.index(".") and em.index('.') - em.index('@') > 1 and em[0] not in ls_spl:
            return True

        else:
            return False

    else:
        print("invalid input")


def password_check(s):#validates the input passwords. Returns Boolean.
    l, u, p, d = 0, 0, 0, 0
    if 5 <= len(s) <= 16:
        for i in s:
            if i.islower():  # counting lowercase alphabets.
                l += 1
            if i.isupper():  # counting uppercase alphabets.
                u += 1
            if i.isdigit():  # counting digits.
                d += 1
        for i in range(len(s)):  # counting the special characters.
            x = s[i]
            if x in ls_spl:
                p += 1
                return True
            else:
                pass
    if l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s):
        return True
    else:
        return False


ls_spl = ['!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
          '@', '[', '\\', "\]", '^', '_', '`', '{', '|', '}', '~']
# A list of special characters.


def get_inputs():# gets input of mail id and password and validates them, Return Boolean.
    email_id = input("Enter the Email_ID: ")
    password_pass = input("Enter the password: ")
    if "@" in email_id and "." in email_id and email_id_check(email_id) == True and \
            password_check(password_pass):
        flag = True
    else:
        flag = False

    return email_id, password_pass, flag


def register_mail():# writes the mail id and password into the file.
    ip = get_inputs()
    email_id = ip[0]
    password_pass = ip[1]
    flag = ip[2]

    if flag == True:
        pass_value = email_id + "," + password_pass
        file = r'E:\Learning_Python\Python\Python_Projects\Project 1\Register_login.csv'
        with open(file, 'a', newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(pass_value.split(","))
            csvfile.close()
        print("You have registered successfully")
    else:
        print("Mail ID or password does not satisfy conditon")


def input_choice():# let's us choose between Register, Login and Exit.
    ch = int(input("Choose 1 for Register\nChoose 2 for login\nChoose 0 for exit\nEnter the choice:"))
    if ch == 1:
        register_mail()
    elif ch == 2:
        out = get_inputs()
        email_id = out[0]
        password_pass = out[1]
        flag = out[2]
        if flag == True:
            login_check(email_id, password_pass)
        else:
            print("Mail ID or password does not satisfy conditon")
    elif ch == 0:
        exit()
    else:
        print('Enter a valid input: ')
    return ch


def login_check(id, pwd): # Checks for the credentials in the file.
    file = r'E:\Learning_Python\Python\Python_Projects\Project 1\Register_login.csv'
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        username = id
        password = pwd
        for row in csv_reader:
            if row[0] == username and row[1] == password:
                login = True
                break
            elif row[0] == username and row[1] != password:
                forget_pass()
                print(row[1])
            else:
                login = False

    if login == True:
        print("You are now logged in!")
    else:
        print("There is no such account! Kindly register new account!")


def forget_pass(): #retrieves the password for the correct mail ID.
    id = input("Enter your mail ID to retrive password: ")
    file = r'E:\Learning_Python\Python\Python_Projects\Project 1\Register_login.csv'
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        username = id
        for row in csv_reader:
            if row[0] == username:
                return row[1]
            else:
                return 0


while True: # runs the total application.
    ch = input_choice()
    if ch == 0:
        break
