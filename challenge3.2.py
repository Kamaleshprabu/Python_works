class Student:
    def __init__(self,name,roll_number,cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa

def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
    return sorted_students

Students=[Student("rajesh","47",9.8),
          Student("ramkumar","48",7.0),
          Student("naveen","49",9.0),
          Student("prasana","46",10.0),
         ]

sorted_students=sort_students(Students)


for student in sorted_students:
    print("Name : {} ,Roll Number : {}, CGPA : {}".format(student.name,student.roll_number,student.cgpa))
