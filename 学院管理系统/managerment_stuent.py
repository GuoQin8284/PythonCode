from student import Student
class SystemManagermanet():
    def __init__(self):
        self.student_list = []

    def run(self):
        self.show_menu()
        while True:
            menu_num = int(input("请输入功能序号:"))
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.select_student()
            elif menu_num == 3:
                self.update_student()
            elif menu_num == 4:
                self.det_student()
            else:
                print("输入的功能序号不正确，请重新输入")

    @staticmethod
    def show_menu():
        print("1.新增学院\n2.查询学员\n3.修改学员\n4.查看学员")

    def add_student(self):
        name = input("请输入姓名：")
        age = input("请输入性别：")
        self.student_object = Student(name, age)
        self.student_list.append(self.student_object)
        print(self.student_list)

    def select_student(self):
        print([i.age for i in self.student_list])

    def update_student(self):
        pass

    def det_student(self):
        pass