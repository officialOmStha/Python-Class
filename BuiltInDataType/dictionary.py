student = {
    "name" : "Om",
    "age" : 20,
    "course" : "BITM"
}

student["name"] = "Honey"

print(student)

print(student["course"])
print(student.get("age"))

key = ("Roll", "Section")
value = (1, "A")

student.update({k : v for k,v in zip(key, value)})

print(student)

