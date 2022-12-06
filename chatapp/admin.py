from django.contrib import admin
from chatapp.models import Room, Message,ChatRoomParticipant
# Register your models here.

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(ChatRoomParticipant)


