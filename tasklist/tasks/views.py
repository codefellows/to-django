from django.shortcuts import render

# Create your views here.
def home_view(request):
    incomplete = Task.incomplete_tasks.all()
    complete = Task.objects.all().filter(complete=True)
    context = {'incomplete': incomplete, 'complete': complete}
    return render(request, "tasks/home.html", context=context)
