dt={"Harsh":80,"Bhuvan":85,"Raj":75}
name=input("Enter the student's name: ")
if name in dt.keys():
    print(name+"'s marks:",dt[name])
else:
    print("Student not found.")
