# Importing the 'render' function to render templates and the 'redirect' function to redirect to other URLs
from django.shortcuts import render, redirect

# Importing the 'Expense' and 'Category' models from the models file to work with expenses and categories
from .models import Expense, Category

# Importing the 'ExpenseForm' from the forms file to handle form submission for expenses
from .forms import ExpenseForm


# View function for the home page
def home(request):
    # Querying all expenses from the database and ordering them by date in descending order
    expenses = Expense.objects.all().order_by('-date')

    # Rendering the 'home.html' template and passing the list of expenses to be displayed
    return render(request, 'home.html', {'expenses': expenses})


# View function for adding a new expense
def add_expense(request):
    # Checking if the request is a POST (i.e., a form submission)
    if request.method == 'POST':
        # Creating an instance of the form with the submitted data
        form = ExpenseForm(request.POST)

        # Checking if the form data is valid (passes validation rules)
        if form.is_valid():
            # Saving the form data to the database as a new Expense record
            form.save()

            # Redirecting the user back to the 'home' page after successfully adding the expense
            return redirect('home')
    else:
        # If the request is not a POST (i.e., the user is visiting the page), create an empty form
        form = ExpenseForm()

    # Rendering the 'add_expense.html' template and passing the form to be displayed on the page
    return render(request, 'add_expense.html', {'form': form})
