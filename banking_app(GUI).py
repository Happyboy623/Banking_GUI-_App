from tkinter import*
import os
import csv
import sys
import re

window = Tk()

window.title("Happyboy's Banking Application")
window.configure(bg='green')
window.geometry("500x500")

def fin_sign():

    global name

    name = TempName.get()

    email = TempEmail.get()
    password = TempPw.get()
    accounts = os.listdir()

    if name == "" or email == "" or password == "":
        notifications.config(
            fg='red', text="There must be an entry in every field")
        return

    if len(password) < 8:
        notifications.config(
            fg='red', text="Password needs to be at least 8 CHARACTERS long")
        return
    elif re.search('[0-9]', password) is None:
        notifications.config(
            fg='red', text="Make sure your PASSWORD has NUMBERS in it")
        return
    elif re.search('[A-Z]', password) is None:
        notifications.config(
            fg='red', text="Make sure your PASSWORD has a UPPER_CASE LATTERS in it")
        return
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    if(re.search(regex, email)) is None:
        notifications.config(
            fg='red', text="Your Email address is not valid. PLEASE enter the valid Email Address!")
        return

    for check_name in accounts:
        newfile = name + '.csv'
        if newfile == check_name:
            notifications.config(
                fg='red', text="Sorry somebody already has that USERNAME!")
            return

        else:
            with open(newfile, "w", newline="") as File:
                balance = 0
                writer = csv.writer(File)
                writer.writerow([name])
                writer.writerow([email])
                writer.writerow([password])
                writer.writerow([balance])
            File.close()
            notifications.config(
                fg='green', text="Congratulations Your Account is successfully Created")

def Register():
    global TempName
    global TempEmail
    global TempPw
    global notifications
    TempName = StringVar()
    TempEmail = StringVar()
    TempPw = StringVar()

    global RegisterScreen
    RegisterScreen = Toplevel(window)
    RegisterScreen.geometry("500x450")
    RegisterScreen.title("Register")
    Label(RegisterScreen, text="Set Up Your Account \n And Enjoy the Service!",
          font=(20)).grid(row=0, sticky=N, pady=10)
    Label(RegisterScreen, text="Name", font=(
        20)).grid(row=2, sticky=W, pady=10)
    Label(RegisterScreen, text="Email", font=(
        20)).grid(row=3, sticky=W, pady=10)
    Label(RegisterScreen, text="Password", font=(
        20)).grid(row=4, sticky=W, pady=10)

    Entry(RegisterScreen, textvar=TempName).grid(row=2, column=0)
    Entry(RegisterScreen, textvar=TempEmail).grid(row=3, column=0)
    Entry(RegisterScreen, textvar=TempPw, show="*").grid(row=4, column=0)

    Button(RegisterScreen, text="Confirm", command=fin_sign,
           font=(20)).grid(row=7, sticky=N, pady=10)
    Button(RegisterScreen, text="Show Password", command=showsign,
           font=(18)).grid(row=6, sticky=W, pady=10)
    Button(RegisterScreen, text="Hide Password", command=hidesign,
           font=(18)).grid(row=6, sticky=E, pady=10)
    notifications = Label(RegisterScreen, font=(20))
    notifications.grid(row=8, sticky=N, pady=10)

def showsign():
    Entry(RegisterScreen, textvar=TempPw, show="").grid(row=4, column=0)

def hidesign():
    Entry(RegisterScreen, textvar=TempPw, show="*").grid(row=4, column=0)

def showsignlog():
    Entry(LogInScreen, textvar=TempLogPw, show="").grid(row=2, column=1)

def hidesignlog():
    Entry(LogInScreen, textvar=TempLogPw, show="*").grid(row=2, column=1)

def dashboard():
    accounts = os.listdir()
    global LogName
    LogName = TempLogName.get()
    LogPw = TempLogPw.get()
    CheckLogName = LogName + '.csv'
    for check_name in accounts:
        if check_name == CheckLogName:
            file = open(check_name, "r")
            file_info = file.read()
            file_info = file_info.split('\n')
            CorrectPassword = file_info[2]

            if LogPw == CorrectPassword:
                name = LogName
                LogInScreen.destroy()
                dashboard = Toplevel(window)
                dashboard.geometry("500x450")
                dashboard.title("Dashboard")
                Label(dashboard, text="DASHBOARD:", font=(
                    20)).grid(row=0, sticky=W, pady=5)
                Label(dashboard, text="Welcome "+LogName,
                      font=(20)).grid(row=0, sticky=N, pady=5)
                Button(dashboard, text="Account Info", width=30, font=(
                    20), command=account_info).grid(row=2, sticky=N, pady=10)
                Button(dashboard, text="Deposit", width=30, font=(20),
                       command=deposit).grid(row=5, sticky=N, padx=10, pady=10)
                Button(dashboard, text="Withdraw", width=30, font=(20),
                       command=withdraw).grid(row=6, sticky=N, padx=10, pady=10)
                Button(dashboard, text="Check Balance", width=30, font=(
                    20), command=balance).grid(row=7, sticky=N, padx=10, pady=10)

                return

            else:
                LogNotifications.config(fg="red", text="Wrong password!")
                return

    LogNotifications.config(fg="red", text="No account found!")

def account_info():
    file = open(LogName + ".csv", "r")
    data = file.read()
    info = data.split('\n')
    name_info = info[0]
    email_info = info[2]
    pw_info = info[1]

    info = Toplevel(window)
    info.geometry("500x450")
    info.title("Account Info")
    Label(info, bg='orange', text="Account Info", font=(
        40)).grid(row=0, sticky=N, pady=10, padx=30)
    Label(info, bg='orange', text="Name: " + name_info,
          font=(40)).grid(row=1, sticky=W, pady=10, padx=30)
    Label(info, bg='orange', text="Password: " + email_info,
          font=(40)).grid(row=2, sticky=W, pady=10, padx=30)
    Label(info, bg='orange', text="Email: " + pw_info,
          font=(40)).grid(row=3, sticky=W, pady=10, padx=30)

def deposit():
    global rands_to_enter
    global deposit_notifications
    global current_rands_label
    rands_to_enter = StringVar()
    file = open(LogName + ".csv", "r")
    data = file.read()
    details = data.split('\n')
    balance_details = details[3]
    deposit_display_screen = Toplevel(window)
    deposit_display_screen.geometry("500x450")
    deposit_display_screen.title("Deposit")
    Label(deposit_display_screen, text="Deposit amount: ",
          font=(20)).grid(row=0, sticky=N, pady=10)
    current_rands_label = Label(
        deposit_display_screen, text="Your currently balance is now:R "+balance_details, font=(20))
    current_rands_label.grid(row=0, sticky=N, pady=10)
    Label(deposit_display_screen, text="Deposit: ",
          font=(20)).grid(row=2, sticky=W, pady=10)
    deposit_notifications = Label(deposit_display_screen, font=(20))
    deposit_notifications.grid(row=4, sticky=N, pady=5)
    Entry(deposit_display_screen, textvariable=rands_to_enter).grid(row=2, column=1)
    Button(deposit_display_screen, text="Confirm", font=(20),
           command=fin_deposit).grid(row=3, sticky=W, pady=5)

def fin_deposit():
    if rands_to_enter.get() == "":
        deposit_notifications.config(
            text="Sorry...you must enter something into the Bank", fg="red")
        return
    if float(rands_to_enter.get()) <= 0:
        deposit_notifications.config(
            text="Sorry...you must enter a number greater than 0", fg="red")
        return
    file = open(LogName + '.csv', 'r+')
    data = file.read()
    info = data.split('\n')
    old_balance = info[3]
    new_balance = old_balance
    new_balance = float(new_balance) + float(rands_to_enter.get())
    new_balance = str(round(new_balance, 2))
    data = data.replace(old_balance, str(new_balance))
    file.seek(0)
    file.truncate(0)
    file.write(data)
    file.close()
    current_rands_label.config(
        text="Your now current balance is:R"+str(new_balance), fg="green")
    deposit_notifications.config(
        text="Deposit was successfully made", fg="green")


def withdraw():
    global withdraw_rands
    global withdraw_notifications
    global withdraw_rands_label
    global rands_to_enter
    global withdraw_display_screen
    withdraw_rands = StringVar()
    file = open(LogName + ".csv", "r")
    data = file.read()
    details = data.split('\n')
    balance_details = details[3]
    withdraw_display_screen = Toplevel(window)
    withdraw_display_screen.geometry("500x450")
    withdraw_display_screen.title("Withdraw")
    current_rands_label = Label(
        withdraw_display_screen, text="Deposit amount: ", font=(20))
    current_rands_label.grid(row=0, sticky=N, pady=10)
    Label(withdraw_display_screen, text="withdraw: ",
          font=(20)).grid(row=2, sticky=W, pady=10)
    withdraw_rands_label = Label(
        withdraw_display_screen, text="You currently have:R "+balance_details, font=(20))
    withdraw_rands_label.grid(row=0, sticky=N, pady=5)
    withdraw_notifications = Label(withdraw_display_screen, font=(20))
    withdraw_notifications.grid(row=4, sticky=N, pady=5)
    Entry(withdraw_display_screen, text=withdraw_rands).grid(row=2, column=1)
    Button(withdraw_display_screen, text="Confirm", font=(20),
           command=fin_withdraw).grid(row=3, sticky=W, pady=5)

def fin_withdraw():
    if withdraw_rands.get() == "":
        withdraw_notifications.config(
            text="Sorry...you must enter something into the Bank", fg="red")
        return
    if float(withdraw_rands.get()) <= 0:
        withdraw_notifications.config(
            text="Sorry...you must enter a number greater than 0", fg="red")
        return
    file = open(LogName + '.csv', 'r+')
    data = file.read()
    info = data.split('\n')
    old_balance = info[3]
    new_balance = old_balance
    new_balance = float(new_balance) - float(withdraw_rands.get())
    new_balance = str(round(new_balance, 2))
    if float(new_balance) < 0:
        withdraw_notifications.config(
            text="Sorry...you can not WITHDRAW more than you have", fg="red")
        return
    data = data.replace(old_balance, str(new_balance))
    file.seek(0)
    file.truncate(0)
    file.write(data)
    file.close()
    withdraw_rands_label.config(
        text="You currently have:R "+str(new_balance), fg="green")
    withdraw_notifications.config(
        text="The withdrawal was successfully processed", fg="green")

def balance():
    file = open(LogName + ".csv", "r")
    data = file.read()
    info = data.split('\n')
    global balance_info
    balance_info = info[3]
    balance = Toplevel(window)
    balance.geometry("500x450")
    balance.title("Ammount of money in the Bank")
    Label(balance, bg='green', text="Balance:R " + balance_info,
          font=(40)).grid(row=3, sticky=W, pady=10, padx=30)

def log_in():
    global TempLogName
    global TempLogPw
    global LogNotifications
    global LogInScreen
    TempLogName = StringVar()
    TempLogPw = StringVar()
    LogInScreen = Toplevel(window)
    LogInScreen.title("Log In")
    LogInScreen.geometry("500x450")
    Label(LogInScreen, text="Welcome Back! Log into your Account!",
          font=(50)).grid(row=0, sticky=N)
    Label(LogInScreen, text="Username", font=(20)).grid(row=1, sticky=W)
    Label(LogInScreen, text="Password", font=(20)).grid(row=2, sticky=W)
    LogNotifications = Label(LogInScreen, font=(20))
    LogNotifications.grid(row=4, sticky=N)
    Entry(LogInScreen, textvar=TempLogName).grid(row=1, column=1, padx=5)
    Entry(LogInScreen, textvar=TempLogPw,
          show="*").grid(row=2, column=1, padx=5)
    Button(LogInScreen, text="Login", command=dashboard, width=40,
           font=(20)).grid(row=7, sticky=W, pady=5, padx=5)
    Button(LogInScreen, text="Show Password", command=showsignlog,
           font=(18)).grid(row=6, sticky=W, pady=10)
    Button(LogInScreen, text="Hide Password", command=hidesignlog,
           font=(18)).grid(row=6, sticky=E, pady=10)

Label(window, bg='orange', text="Welcome to Happyboy's Banking Application \n Register to start Banking with US",
      font=(70)).grid(row=0, sticky=N, pady=50, padx=30)

Button(window, bg='yellow', text="Register", font=(40), width=30,
       height=2, command=Register).grid(row=4, sticky=N, pady=10, padx=120)

Button(window, bg='yellow', text="Login", font=(40), width=30, height=2,
       command=log_in).grid(row=5, sticky=N, pady=10, padx=120)

window.mainloop()