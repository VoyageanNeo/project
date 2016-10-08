from django.conf import settings
from django.shortcuts import render
from django.http import Http404
from django.contrib import messages
from .forms import SignupForm, ContactForm
from django.core.mail import send_mail


def home(request):
    if not request.user.is_authenticated():
        raise Http404
    title="News letter %s" % (request.user)
    form=SignupForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
    context={
        "title":title,
        "form":form,
    }
    return render(request, 'home.html', context)
def contact(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        # after you checked if form is valid or not, you can call cleaned_data
        form_email=form.cleaned_data.get("email")
        form_message=form.cleaned_data.get("message")
        form_full_name=form.cleaned_data.get("full_name")
        subject = "Confirmation for register"
        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email, form_email]
        contact_messages= "%s, %s via %s"%(form_full_name, form_message,form_email)
        send_mail(
            subject,
            contact_messages,
            from_email,
            to_email,
            fail_silently=False,
        )
    context = {
        "form": form,
    }
    return render(request, 'contact.html', context)