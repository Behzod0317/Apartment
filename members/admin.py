from django.contrib import admin

# Register your models here.
from .models import Member

class MemberAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "joined_data")
  repopulated_fields = {"slug": ("firstname","lastname")}

admin.site.register(Member, MemberAdmin)


  
