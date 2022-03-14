from school_app.models import Student
import datetime
from django.db.models import Q

# select all students where birthdates id not null
        # data = Student.objects.filter(~Q(birthdate=None))
        # print(data)

# select all where name contains a j or J
        # data = Student.objects.filter(name__icontains="%J%")
        # print(data)



# Student.objects.all().delete()  - delete all from db


# new_student = Student()
# new_student.name = "Bailey Gates"
# new_student.email = "billmoney@microsoft.com"
# new_student.birthdate = datetime.datetime.now()
# new_student.save()

# new_student = Student()
# new_student.name = "Stella Jobs"
# new_student.email = "stellamoney@apple.com"
# new_student.birthdate = datetime.datetime.now()
# new_student.save()

# Add new records -
    # through shell 
# through fixtures folder
    # 'python manage.py loaddata students<filename>'
    
    # 'python manage.py dumpdata school_app.student > student_dumpdata.json' - extracts db data converts to json

# the admin panel
# 'python manage.py createsuperuser'
# 'admin' '' 'password' y
# 
# 'admin.site.register(Student)' # provide access to the Student model in admin panel