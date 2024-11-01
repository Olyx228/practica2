from django.contrib import admin
from .models import Request, Category

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'user']
    list_filter = ['status', 'created_at']
    readonly_fields = ('title', 'description', 'category', 'user')
    search_fields = ['title', 'description', 'user__username']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is not None:  # Проверяем, что объект существует
            print(f"Статус заявки: {obj.status}")  # Выводим статус в консоль
            if obj.status == 'new':  # Проверяем статус
                form.base_fields['comment'].disabled = True  # Делаем поле комментариев недоступным
        return form

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

