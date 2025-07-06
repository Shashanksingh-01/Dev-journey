def print_student(student):
    for key in student:
        print(key,":",student[key])

student1= {
    "name":"Shashank Singh",
    "age": 18,
    "branch":"Cse IoT"
}
student2={
    "name":"ANANT KUMAR",
    "age" : 19,
    "branch" : "Cse IoT"
}
print_student(student1)
