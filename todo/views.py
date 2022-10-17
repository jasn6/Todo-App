from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, 'home.html',context)

def create_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request, 'create-todo.html',context)

def edit_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form":form}
    return render(request,"create-todo.html",context)

def delete_todo(request,pk):
    todo = Todo.objects.get(id = pk)
    if request.method == "POST":
        todo.delete()
        return redirect('home')
    return render(request,"delete.html",{"obj":todo})