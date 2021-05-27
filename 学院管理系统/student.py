class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.stu_data = self.load_student_info("./stu_data.txt")

    def __str__(self):
        data = f'{self.name}, {self.age}'
        print(type(data))
        return data

    def load_student_info(self,file_path):
        stu_file = open(f"{file_path}","w+",encoding="utf-8")
        stu_data = stu_file.readlines()
        return stu_data