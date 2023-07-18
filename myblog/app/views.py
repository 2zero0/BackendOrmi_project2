from django.views import View
from django.shortcuts import render, redirect

class IndexMain(View):
    def get(self, request):
        return render(request, 'index.html')