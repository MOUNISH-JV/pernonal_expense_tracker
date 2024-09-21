# Importing the 'models' module from Django's database library to define database models
from django.db import models


# Defining the 'Category' model to represent categories of expenses
class Category(models.Model):
    # Defining a CharField to store the name of the category with a max length of 100 characters
    name = models.CharField(max_length=100)

    # String representation of the 'Category' model, returning the category name
    def __str__(self):
        return self.name


# Defining the 'Expense' model to represent an individual expense
class Expense(models.Model):
    # ForeignKey establishes a relationship with the 'Category' model
    # on_delete=models.CASCADE means if a category is deleted, the associated expenses are also deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Defining a CharField to store a description of the expense with a max length of 255 characters
    description = models.CharField(max_length=255)

    # DecimalField to store the amount of the expense, allowing up to 10 digits in total with 2 decimal places
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # DateField to store the date when the expense occurred
    date = models.DateField()

    # String representation of the 'Expense' model, returning a string that includes the category and amount
    def __str__(self):
        return f"{self.category} - {self.amount}"
