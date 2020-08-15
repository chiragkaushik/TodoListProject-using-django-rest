from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class TodoList(BaseModel):
    name = models.CharField(max_length=30)

    # created_by = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Access(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    list_id = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    permission_type = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)


class TodoItem(BaseModel):
    list_id = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name = 'list_id_interaction')
    heading = models.CharField(max_length=30)
    scheduled_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.heading



