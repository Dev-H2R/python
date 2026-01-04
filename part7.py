# tuple set dictionary
t = (10, 20, 30)
print(t)

#access 
print(t[0])
print(t[-1])

#loop tuple
for i in t:
    print(i)

#dictionary
student = {
    "name": "Devashish",
    "age": 20,
    "city": "Pune"
}

print(student["name"])
print(student.get("age"))

#modify dict
student["age"] = 21
student["college"] = "XYZ"
#loop dict
for key in student:
    print(key, student[key])

#dict func
print(student.keys())
print(student.values())
print(student.items())
