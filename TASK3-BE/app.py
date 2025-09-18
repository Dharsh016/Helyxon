from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/students/{id}")
def get_student(id: int):
    
    student = {
        1: {"name": "Dharsh", "age": 21},
        2: {"name": "Meera", "age": 21},
        3: {"name": "John", "age": 22}
    }
    return student.get(id, {"error": "Student not found"})
