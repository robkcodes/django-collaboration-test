from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm


def home_page(request):
    """
    Returns Hello Message
    """

    post_form = PostForm()
    return render(
        request,
        "home/index.html",
        {
            "post_form": post_form,
        },
    )
