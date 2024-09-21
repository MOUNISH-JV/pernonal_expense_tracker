# Importing the 'forms' module from Django to create forms
from django import forms

# Importing the 'Expense' model from the models file to use it in the form
from .models import Expense


# Defining a form class 'ExpenseForm' that inherits from 'forms.ModelForm'
class ExpenseForm(forms.ModelForm):
    # Meta class defines metadata for the form
    class Meta:
        # Specifying the model that this form is based on (Expense model)
        model = Expense

        # Defining the fields from the Expense model that will be included in the form
        fields = ['category', 'description', 'amount', 'date']
