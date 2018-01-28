from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from todoapp.core.models import TodoList, Category   
from todoapp.core.forms import SignUpForm     

from django.conf import settings

@login_required
def home(request):

	todos = TodoList.objects.filter(user_id = request.user.id) 
	categories = Category.objects.filter(user_id = request.user.id) 

	if request.method == "POST": 
		if "categoryAdd" in request.POST: 
			user_id = request.user.id 
			category = request.POST["category"]  
			Todo = Category(user_id = user_id,name=category)
			Todo.save() 
			return redirect("/") 

		if "categoryDelete" in request.POST: 
			user_id = request.user.id 
			categoryid = request.POST["categoryid"]  
			category_item = Category.objects.get(id=int(categoryid)) 
			category_item.delete() 
			return redirect("/")       

		if "taskAdd" in request.POST: 
			user_id = request.user.id 
			title = request.POST["description"] 
			date = str(request.POST["date"]) 
			category = request.POST["category_select"] 
			content = title + " -- " + date + " " + category 
			Todo = TodoList(user_id = user_id,title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save() 
			return redirect("/")    
		
		if "taskDelete" in request.POST: 
			checkedlist = request.POST["checkedbox"] 
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) 
				todo.delete() 
	return render(request, 'home.html',{"todos": todos, "categories":categories})


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
