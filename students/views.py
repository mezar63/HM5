from django.http import JsonResponse

from faker import Faker

from .models import Student


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def create_student():
    fake = Faker('uk')

    student = Student.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date()
    )

    return {
        "id": student.id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "birth_date": student.birth_date
    }


def generate_student(request):
    student = create_student()
    return JsonResponse(student)


def generate_students(request):
    count = request.GET.get('count')
    if not count or not is_int(count):
        return JsonResponse({
            "error": "Параметр count не корректный"
        })

    count = int(count)

    if count <= 0 or count > 100:
        return JsonResponse({
            "error": "Параметр count должен быть больше 0 или меньше, равно 100"
        })

    students = [create_student() for i in range(count)]

    return JsonResponse({
        "students": students
    })
