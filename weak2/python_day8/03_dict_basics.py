student={"name":"shashank",
         "age":18,
         "branch":"CSE"}
print(student)
print(student["name"])
print(student["age"])
# update age 
student["age"]=19
print(student)

# add city
student["city"]="Patna"
print(student)
# remove
student.pop("branch")