""" B. Create a console application for an IT Academy with the
following features:
a) The academy program should have a fixed course of study.
b) If a new student is interested in the academy program the student can
inquiry about the course of study.
c) Student Registration with Rs. 20000 (deposit). Students are allowed to
pay in two installments with Rs. 10000 each.
d) Display all the student’s information from the academy with their payments
and remaining payments.
e) Update the student information if needed.
f) Delete the student information if he/she left the program.
g) Return the deposit amount (Rs. 20000) to the students after the
successful completion of the course and check the balance.
Remember it should be a full feature CONSOLE APP. You can store
the course of study and the student’s detail in your preferred file
format (.csv, .txt, etc).
Ignore the permissions for now. Anyone who runs the script is allowed to
access all the features. Develop the app with OOP Approach."""


class ItAcademy:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        f = open('studentInfo.txt')
        with open('studentInfo.txt', "w") as f:
            to_write = ("Students name: {0} The student has paid: {1}".format(self.name, self.balance))
            f.write(to_write)

    def __del__(self):
        pass

    def student_info(self):
        print("The students name is", self.name)
        if self.balance == 20000:
            print("The student has opt in to pay the registration fee fully and does not have any payment pending")
        elif self.balance == 10000:
            print("The student has opt in to pay the registration fee in installments")
        else:
            print("The students has completed the course. Deposit Returned!!!")

    def course_info(self):
        print("======WELCOME TO IT ACADEMY======")
        print("\n\n In this class you will learn about \n")
        print("1. Full stack web development")
        print("2. HTML, CSS, JS and ES6")
        print("3. Python Programming")
        print("4. Backend Framework: Django")
        print("5. Django REST Framework")
        print("6. Frontend Library React")

    def update_info(self, name, balance):
        self.name = name
        self.balance = self.balance + balance

    def del_info(self):
        if self.balance == 20000:
            with open("studentInfo.txt", "r") as f:
                lines = f.readlines()
            with open("studentInfo.txt", "w") as f:
                for line in lines:
                    print(self.name, "is being removed off the list")
                    to_delete = "Students name: {} The student has paid: {}".format(self.name, self.balance)
                    if line.strip("\n") != to_delete:
                        f.write(line)
        else:
            print("Payments Remaining!!!")

    def return_deposit(self):
        self.balance = 0
        print("Balance has been returned to the student")


student1 = ItAcademy('Sakar Poudel', 20000)
student1.del_info()
student2 = ItAcademy('Keshav', 10000)
student2.del_info()



