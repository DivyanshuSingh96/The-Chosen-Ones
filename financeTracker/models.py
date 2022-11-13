from django.db import models
from django.contrib import admin

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField("Email Address", max_length=200, null=True)
    date_created = models.DateTimeField("Created On", auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class Money(models.Model):

    income = models.FloatField(null=True)
    expense = models.FloatField(null=True)

    # savings = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

    def calculate(self):
        return f"{self.income - self.expense}"

    def __str__(self):
        return f"{self.calculate()}"

    net_worth = __str__    
    __str__.short_description = "Net Worth"

    # submit = models.Subquery(f"SELECT {income - expense} FROM {Money}")

    # def __str__(self):
    #     return f"{self.income} {self.expense} {self.calculate()} {self.date_created.date()}"
    # __str__.short_description = "Net Worth"

    # list_display = ("Income", "Expense", "Net Worth", "Created On")
# @admin.register(Money)
# class DataAdmin(admin.ModelAdmin):
#     list_display = ("Income", "Expense", "Net Worth", "Created On")
#     list_filter = ('Income',)

#     @admin.display(description='Name')
#     def branch_name(self):
#         return self.Money.income

    # def __sub__(self):
    #     return f"{((self.income - self.expense) / 100).round(2)}"



