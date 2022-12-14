from django.shortcuts import render
from .models import lugat

# Create your views here.
def index(request):
    suz = request.GET.get('q','')
    if suz and suz !='':
        natija = lugat.objects.filter(sotix=suz).all()
    #elif (suz and suz !='') and (bn == 'Gektar'):
     #   natija = lugat.objects.filter(inglizcha__contains=suz, kom='lalaimi').all()
    else:
        natija = None
    return render(request, 'index.html', {'q':suz, 'natija':natija})