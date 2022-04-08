class login:
    def __init__(self):
        self.credintials = {}
    def register(self, username, password):
        self.credintials[username] = password

    def check(self, user, pas):
        print(self.credintials )
        if user in self.credintials.keys() and pas == self.credintials[user]:
            print("Login success!")
        else:
            print('Wrong Username or Password')
s = login()
Stop = False

while Stop == False:
    print("*********  Welcome  *******")
    choice = (input('Enter your Choice : \n 1. Register new Account  \n 2. Login   \n 3. quit \n'))
    # Calling functions with that class object
    if choice == '1':
        Name = (input('Please enter username: '))
        Pword= (input('Please enter password: '))
        s.register(Name, Pword)

    if choice == '2':
        LoginInfoUser = (input('Please enter Username: '))
        LoginInfoPassword = (input('Please enter Password: '))
        s.check(LoginInfoUser,LoginInfoPassword)
    if choice == '3':
        print("Exit!")
        Stop =True