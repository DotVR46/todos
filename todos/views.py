from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, ToDo
from .forms import ToDoForm


# Create your views here.
def todo_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    todos = ToDo.objects.all()
    if request.method == 'POST':
        
        todo = get_object_or_404(ToDo, id=request.POST['todo_id'])
        todo.completed = not todo.completed
        todo.save()
        return redirect('/')
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        todos = todos.filter(category=category)
    return render(request, 'todos/todo_list.html',
                {'category': category,
                'categories': categories,
                'todos': todos})

def create(request):
    form = ToDoForm()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            todo = ToDo(title=cd['title'],
                        description=cd['description'],
                        category=cd['category'])
            todo.save()
        return redirect('/')

    return render(request, 'todos/create.html', {'create_form': form})




