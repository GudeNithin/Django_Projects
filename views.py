from django.shortcuts import render

# Create your views here.
def task_view(request):
    context = {"dynamic_data": "This is some dynamic data!"}
    return render(request, 'task.html', context)