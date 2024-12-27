from django.contrib import admin
from .models import Message
from .models import IPLog

class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'timestamp')
    search_fields = ('name', 'content')  # Allows searching for messages by name/content
    list_filter = ('timestamp',)  # Filters messages by timestamp
    ordering = ('-timestamp',)  # Orders messages by the most recent first

admin.site.register(Message, ChatAdmin)
admin.site.register(IPLog)
