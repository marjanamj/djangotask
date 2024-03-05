from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_mame = models.CharField(max_length=50)
    email = models.EmailField
    age = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name

class Course():
    name = models.CharField(max_length=100)
    description = models.TextField
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


# # # 6) Создайте необходимые миграции для данных моделей с 
# омощью команды python manage.py makemigrations 
# # # 7) Примените миграции к базе данных с помощью 
# команды python manage.py makemigrations  8) Проверьте работу моделей и связей, 
# создав несколько объектов моделей Student и Course в Django-админке 
# или через интерпретатор Python. 
# # # Коротко о том, как должно все работать:
# # '''
