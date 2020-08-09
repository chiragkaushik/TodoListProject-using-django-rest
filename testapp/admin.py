from django.contrib import admin
from testapp.models import BaseModel,TodoList, Access, TodoItem
# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'created_at', 'updated_at', 'is_active']

class AccessAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'list_id', 'permission_type', 'created_at', 'updated_at', 'is_active' ]

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'list_id', 'heading', 'scheduled_on', 'created_at', 'updated_at', 'is_active']

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Access, AccessAdmin)
