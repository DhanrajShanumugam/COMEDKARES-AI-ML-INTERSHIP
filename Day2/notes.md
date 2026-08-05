functions:
def multiply(a,b):
     print(a*b)
     return a*b
result=multiply(4,5)
print(result)
list:
car=["Bmw","audi","ferrari","rollsroyces","jaguar"]
print(car[2])
car.append("fortuner")
print(car)
car.remove("jaguar")
print(car)
print(car)
tuple:
days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days[0])
print(days[-1])
print(len(days))
dictionary:
student={
    "name":"dhanraj",
    "usn":1234,
    "branch":"CSE",
    "cgpa":9.5
}
for key,value in student.items():
    print(key,":",value)
    
    -->student management system:
    subjects=("python","sql","ai")
student=[]
def add_student(name,age):
    student_details={
        "name":"dhanraj",
        "age":20,
        "subject":subjects
    }
    student.append(student_details)
add_student("name","age")    
#add_student("Dhanraj",20)
#add_student("vinooj",21)
for student_details in student:
    print(student_details)
        
    
