from django.contrib import admin

# Register your models here.

# from financeTracker.models import Money
# from financeTracker.models import Customer
from .models import *

admin.site.register(Customer)
# admin.site.unregister(Money)

@admin.register(Money)
class DataAdmin(admin.ModelAdmin):
    list_display = ("income", "expense", "net_worth", "date_created")
    ordering = ("income",)
    search_fields = ("income", "date_created")
    # list_filter = ('Income',)

#     @admin.display(description='Name')
#     def branch_name(self):
#         return self.Money.__str__

# admin.site.register(Money, DataAdmin)