people=[
    {"name":"Shashank singh","age":18},
    {"name":"Aman","age":19},
    {"name":"Ayush","age":23}
    ]
def find_person(name):
    for person in people:
        if person["name"]==name:
            return person
    return None

result=find_person("Aman")
print(result)