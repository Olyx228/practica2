from django.contrib import admin
from .models import Request, Category


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'user']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    readonly_fields = ('title', 'description', 'category', 'user')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if obj is not None:  # Проверяем, что объект существует
            print(f"Статус заявки: {obj.status}")  # Выводим статус в консоль

            # Проверка статуса для поля комментариев
            if obj.status == 'new':
                form.base_fields['comment'].disabled = True  # Делаем поле комментариев недоступным

            # Проверка статуса для поля фото
            if obj.status == 'completed':
                form.base_fields['photo'].required = True  # Делаем поле фото обязательным
                form.base_fields['comment'].disabled = True
                form.base_fields['status'].disabled = True
                form.base_fields['photo'].disabled = True

            else:
                form.base_fields['photo'].required = False  # В остальных случаях поле не обязательно

        return form


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']