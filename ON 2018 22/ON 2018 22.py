s_name = []
s_age = []
s_id = []
s_runs = []
s_pb = []
s_edate = []
s_ddate = []

id = 1000

def inputs():
    global age, name
    name = input("Student's Name: ")
    s_name.append(name)
    age = int(input("student's age: "))
    s_id.append(id)

def validation():
    if age < 4 :
        print("You are too young")
    elif age > 14:
        print("You are too old")
    else: s_name.append(age)


def updates():
    global id
    id = id + 1

inputs()
validation()
updates()