# coding= utf-8
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import Student, Teacher, Group, MemberShip


# Create your views here.
def student_list(request):
    t = loader.get_template("student_list.html")
    # newstu = Student(name="abc", age=10, intime="2011-01-02", gender=1)
    # 等同于 insert 数据库语句
    # newstu.save()
    # studentList = Student.objects.filter(age__lt=30).update(
    #   name="xyz")  # 批量更新信息 等同于update student set name = "xyz" where age<30
    # student = Student.objects.get(id=1)  # age__gt = 15 是大于15的表示 age__gte = 15表示为大于等于15
    # 等同于select * from student
    # __contains   =   like "%%"(数据库选择)
    # student.delete() 删除单个数据
    # student = Student.all().delete() 批量删除数据
    # student.save()  # 保存数据库修改数据
    # studentList = Student.objects.all()
    # teacher = Teacher.objects.get(id=1)
    # studentList = teacher.student_teacher.all()
    group = Group.objects.get(id=1)
    studentList = group.members.all()
    groupList = studentList.group_set.all()
    # MemberShip(group=newGroup, student=newStudent).save()#增加新关系
    c = Context({"studentList": studentList})
    return HttpResponse(t.render(c))
