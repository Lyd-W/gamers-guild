from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def about(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

            return redirect('about')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'about/about.html', context)