from django.shortcuts import render, redirect
from django.contrib import messages
from testapp.models import shorturl
import random, string
# Createing my views here.
def home_page(request):
    urls = shorturl.objects.all()
    return render(request,'testapp/home.html',{'urls':urls})
#random generation of 6 chars
def randomgen():
    return ''.join(random.choice(string.ascii_letters) for _ in range(6))
#Generating the short url
def generate(request):
    if request.method == 'POST':
        #generate
        pass
        if request.POST['original'] and request.POST['short']:
            original = request.POST['original']
            short = request.POST['short']
            check = shorturl.objects.filter(short_query = short)
            if not check:
                newurl = shorturl(
                    original_url = original,
                    short_query = short,
                )
                newurl.save()
                return redirect('/')
            else:
                messages.error(request,'Already exists')
                return redirect('/')
        elif request.POST['original']:
            #generate randomly
            original = request.POST['original']
            generated = False
            while not generated:
                short = randomgen()
                check = shorturl.objects.filter(short_query = short)
                if not check:
                    newurl = shorturl(
                        original_url = original,
                        short_query = short,
                    )
                    newurl.save()
                    return redirect('/')
                else:
                    continue
        else:
            messages.error(request,'empty fields')
            return redirect('/')
    else:
        return redirect('/')
#Count of visits page
def home(request, query = None):
    if not query or query is None:
        return render(request,'home1.html')
    else:
        try:
            check = shorturl.objects.get(short_query = query)
            check.visits = check.visits + 1
            check.save()
            url_redirect = check.original_url
            return redirect(url_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'testapp/home1.html',{'error':"error"})
