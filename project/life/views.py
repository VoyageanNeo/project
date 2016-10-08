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

from .forms import mileStoneForm
from .models import mileStone


def mileStone_create(request):
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
    }
    return render(request, "mileStone_form.html", context)


def mileStone_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }
    return render(request, "post_detail.html", context)


def mileStone_list(request):
    today = timezone.now().date()
    queryset_list = mileStone.objects.all()  # .order_by("-timestamp")
    # input type = 'text'name = 'q'placeholder = 'Search posts'value = '{{ request.GET.q }}'
    context = {
        "object_list": queryset_list,
        "title": "mileStone",
        "today": today,
    }
    return render(request, "post_list.html", context)

def mileStone_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(mileStone, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("life:list")
