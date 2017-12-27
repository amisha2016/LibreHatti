from django.http import HttpResponse
from librehatti.catalog.request_change import request_notify
from .forms import dispatch_Form
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect

def dispatch_view(request):
    if request.method == "POST":

        form = dispatch_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = dispatch_Form()
    return render(request, 'dispatch_register/add_entry.html', {'form': form})

