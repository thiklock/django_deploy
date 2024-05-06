<<<<<<< HEAD
=======

>>>>>>> ea6a124 (git init)
from django.shortcuts import render
from django.http import HttpResponse
import datetime


def homepage(request):
    time_now = datetime.datetime.now()
    html_to_display = f"""
        <html>
            <body>
                <h2>It is now {time_now}</h2>
            </body>
        </html>
    """
    return HttpResponse(html_to_display)