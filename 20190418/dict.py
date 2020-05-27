name_dict = {}
std_info = {}
name = input('请输入学生姓名：')
age  = input('请输入学生年龄：')
sex  = input('请输入学生性别：')
name_dict['name']= name
std_info['age']= age
std_info['sex']= sex
print('第一个字典为：',name_dict,'\n','第二个字典为：',std_info)
name_dict.update(std_info)
print('合并后的字典：',name_dict)
print('合并后的字典长度：',len(name_dict))
name_dict.pop('sex')
print('删除后的字典=',name_dict)

