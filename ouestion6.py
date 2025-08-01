students = {
    "Aarav": ["Math", "Science", "History"],
    "Isha": ["English", "Biology", "Art"],
    "Raj": ["Computer Science", "Math", "Physics"]
}
students["Isha"] = tuple(students["Isha"])
print("Updated student subject preferences:")
for name, subjects in students.items():
    print(f"{name}: {subjects}")

