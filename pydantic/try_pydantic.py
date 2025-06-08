from pydantic import BaseModel, Field

# Define schema using Pydantic
class Student(BaseModel):
    name: str = Field(..., description="The name of the student")
    age: int = Field(..., ge=0, description="The age of the student, must be a non-negative integer")
    grade: str = Field(..., description="The grade of the student")

# Create a new student
new_student = Student(name="John Doe", age=20, grade="A")

# If you want to copy it or assign it to another variable
student = Student(**new_student.dict())

print(student)
