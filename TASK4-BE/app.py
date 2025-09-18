from fastapi import FastAPI

app = FastAPI()


students = [
    {"id": 1, "name": "Dharshini", "age": 21},
    {"id": 2, "name": "Meera", "age": 21},
    {"id": 3, "name": "John", "age": 22},
]


@app.get("/students")
def get_students():
    return students


@app.get("/students/{id}")
def get_student(id: int):
    for s in students:
        if s["id"] == id:
            return s
    return {"error": "Student not found"}
