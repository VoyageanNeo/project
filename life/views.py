try:
    from urllib import quote_plus  # python 2
except:
    pass

try:
    from urllib.parse import quote_plus  # python 3
except:
    pass
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from .forms import mileStoneForm, mileStoryForm, UserForm, UserProfileForm
from .models import mileStone, mileStory
#in views.py
def add_user(request):
    uform = UserForm(request.POST or None)
    pform = UserProfileForm(request.POST or None)
    if uform.is_valid() and pform.is_valid():
        user = uform.save()
        profile = pform.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(profile.get_absolute_url())
    context = {
        "uform": uform,
        "pform": pform,
        "title": "Register",
    }
    return render(request, "register.html", context)

def mileStone_create(request, story_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = mileStoneForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Make your own milestone",
    }
    return render(request, "mileStone_form.html", context)

def mileStone_edit(request, story_id, milestone_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(mileStone, id=milestone_id)
    form = mileStoneForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Edit",
    }
    return render(request, "mileStone_form.html", context)

def mileStone_detail(request, story_id, milestone_id):
    instance = get_object_or_404(mileStone, id=milestone_id)
    # if instance.publish > timezone.now().date() or instance.draft:
    #     if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }
    return render(request, "mileStone_detail.html", context)


def mileStone_delete(request, story_id, milestone_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(mileStone, id=milestone_id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("mileStory:storydetail")

#################################################################################################
def mileStory_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = mileStoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "What's your project?"
    }
    return render(request, "mileStory_form.html", context)

def mileStory_edit(request, story_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(mileStory, id=story_id)
    form = mileStoryForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "What's your project?"
    }
    return render(request, "mileStory_form.html", context)

def mileStory_detail(request, story_id):
    instance = get_object_or_404(mileStory, id=story_id)
    # if instance.publish > timezone.now().date() or instance.draft:
    #     if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    mileStone_query = mileStone.objects.filter(id=story_id)
    # mileStone_query = mileStone.objects.all()
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.storyTitle,
        "instance": instance,
        "share_string": share_string,
        "milestone": mileStone_query,
    }
    return render(request, "mileStordy_detail.html", context)

def my_mileStory_list(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse('mileStory:register'))
    queryset_list = mileStory.objects.filter(user=request.user)  # .order_by("-timestamp")
    # input type = 'text'name = 'q'placeholder = 'Search posts'value = '{{ request.GET.q }}'
    context = {
        "object_list": queryset_list,
        "title": "mileStory",
    }
    return render(request, "mileStory_list.html", context)
def mileStory_list(request):
    today = timezone.now().date()
    queryset_list = mileStory.objects.all()  # .order_by("-timestamp")
    # input type = 'text'name = 'q'placeholder = 'Search posts'value = '{{ request.GET.q }}'
    context = {
        "object_list": queryset_list,
        "title": "mileStory",
        "today": today,
    }
    return render(request, "mileStory_list.html", context)

def mileStory_delete(request, story_id):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(mileStory, id=story_id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("mileStory:storylist")
