from urllib import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages
from .models import Person
from .form import PersonForm
from . import form


def forceenroll(request):
    if not request.user.is_authenticated():
        return render(request, 'enroll.html')
    pass
def person_enroll(request):
    form=PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Failed to create")
    context={
        "form": form,
    }
    return render(request, 'post_form.html', context)

def person_update(request, id):
    instance = get_object_or_404(Person, id=id)
    form=PersonForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Failed to create")
    context = {
        "person": instance,
        "form": form,
        "title": instance.get_name
    }
    return render(request, 'post_form.html', context)
def person_list(request):
    forceenroll(request)
    context = {
        "person_list":Person.objects.all(),
        "title": "List"
    }
    return render(request, 'base.html', context)

def person_detail(request, id=None):
    instance=get_object_or_404(Person, id=id)
    share_string = quote_plus(instance.selfintroduction)
    context={
        "person":instance,
        "title": instance.get_name,
        "share_string":share_string
    }
    return render(request, 'detail.html', context)
def person_delete(request, id=None):
    instance=get_object_or_404(Person, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("welcomehome:list")