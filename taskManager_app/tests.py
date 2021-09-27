from django.test import TestCase
from .models import Task, User

# Create your tests here.


class TestTask(TestCase):

    def setUp(self):
        User.objects.create(name="Jean")
        User.objects.create(name="Arthur")
        Task.objects.create(
            title="title_1",
            description="description_1",
            user_id=1
        )
        Task.objects.create(
            title="title_2",
            description="description_2",
            user_id=1
        )

    def test_task(self):
        task_1 = Task.objects.get(title="title_1")
        task_2 = Task.objects.get(title="title_2")
        user = User.objects.get(name="Jean")
        user_2 = User.objects.get(id=2)
        task_2.user_id = user_2.id
        task = Task.objects.all().filter(user_id=1)
        print(task_1, user, task, task_2.user_id)
