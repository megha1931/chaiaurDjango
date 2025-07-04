from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_about(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_about.html', {'chais':chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity,pk=chai_id) #pk means primary key
    return render(request, 'chai/chai_detail.html', {'chai':chai})