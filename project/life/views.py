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

from .forms import mileStoneForm, mileStoryForm
from .models import mileStone, mileStory


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
        "title": "Make your own milestone"
    }
    return render(request, "mileStone_form.html", context)


def mileStone_detail(request, id=id):
    instance = get_object_or_404(mileStone, id=id)
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


def mileStone_list(request):
    today = timezone.now().date()
    queryset_list = mileStone.objects.all()  # .order_by("-timestamp")
    # input type = 'text'name = 'q'placeholder = 'Search posts'value = '{{ request.GET.q }}'
    context = {
        "object_list": queryset_list,
        "title": "mileStone",
        "today": today,
    }
    return render(request, "mileStone_list.html", context)

def mileStone_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(mileStone, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("mileStory:storydelete")

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


def mileStory_detail(request, story_id):
    instance = get_object_or_404(mileStory, id=story_id)
    # if instance.publish > timezone.now().date() or instance.draft:
    #     if not request.user.is_staff or not request.user.is_superuser:
    #         raise Http404
    mileStone_query = mileStone.parentStory.filter(id=story_id)
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.storyTitle,
        "instance": instance,
        "share_string": share_string,
        "milestone": mileStone_query,
    }
    return render(request, "mileStory_detail.html", context)


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
