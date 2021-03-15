from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, ToDo


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



