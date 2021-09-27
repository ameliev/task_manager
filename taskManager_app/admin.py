from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Task

# Register your models here.


@admin.action(description='mark the tasks as done')
def tasks_done(modeladmin, request, queryset):
    queryset.update(done=1)


@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    list_display = ('title', 'description', 'user', 'done')
    ordering = ('-id',)
    search_fields = ('title', 'user_id__username',)
    list_filter = ('user', 'done',)
    actions = [tasks_done]
    # user_id__username = User.id
    fieldsets = (
        (None,
         {'fields': (('title', 'user'), 'description', 'done', 'created_date')}
         ),
    )

    def get_readonly_fields(self, request, obj=None):
        # This is the case when obj is already created i.e. it's an edit
        if obj:
            return 'user'
        else:
            return ()


class TasksResource(resources.ModelResource):
    class Meta:
        model = Task

# admin.site.register(Task)
