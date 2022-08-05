from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddBB, Test_add_BB, scan_qr_form
from django.views.generic import DetailView, CreateView
from django.http import JsonResponse
from .models import warehouseadapp
from whdb.models import whdb

from django.views.decorators.cache import never_cache

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from pyzbar import pyzbar
import cv2
import pytesseract
from PIL import Image
from django.utils import timezone

# @login_required(login_url='login')
# def index(request):
#     news = warehouseadapp.objects.order_by("-created_at")
#     return render(request,"warehousedbapp/index.html", {"news": news, "title": "Список новостей"})
@login_required(login_url='login')
def index(request):
    yesterday = timezone.now() - timezone.timedelta(1)
    authorid = request.user.id
    if request.user.is_staff == False:
        whdb_data = whdb.objects.filter(\
            author_id = authorid,\
            created_at__gte=yesterday).order_by('-created_at')
        context = {
            "whdb_data": whdb_data, 
            "title": "База данних за 24 години"
        }
        return render(request,"warehousedbapp/index.html", context)
    else:
        whdb_data = whdb.objects.filter(created_at__gte=yesterday).order_by('-created_at')
        context = {
            "whdb_data": whdb_data, 
            "title": "База данних за 24 години"
        }
        return render(request,"warehousedbapp/index.html", context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Помилка в паролі чи в назві користувача!')

    context = {}
    return render(request, "warehousedbapp/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def add_BB(request):
    if request.method == "POST":
        form = scan_qr_form(request.POST)
        if form.is_valid():
            warehouseadapp.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = scan_qr_form()
    return render(request, "warehousedbapp/add_BB.html", {'form': form})

class add_bb_view(CreateView):
    model = warehouseadapp
    form_class = Test_add_BB
    template_name = 'warehousedbapp/add_BB.html'


class qr_code_detect(DetailView):
    model = warehouseadapp
    template_name = 'warehousedbapp/add_bb_step1.html'
    
def post_json(request, *args, **kwargs):
    if kwargs.get('pk', None):
        q = kwargs.get('pk', None)
        queryset = warehouseadapp.objects.all().values('id','title','photo','content', 'qr_decode').filter(id = q) 
        query_list = list(queryset)
        img_add = 'media/' + query_list[0]['photo']
        image = cv2.imread(img_add)
        barcodes = pyzbar.decode(image)
        if barcodes:
            qr_code = {'qr_decode': barcodes[0].data.decode('utf-8'), 'id': '', 'title': '', 'photo': '', 'content': ''}
        else: qr_code = {'qr_decode': '0'}
        query_list.append(qr_code)
    return JsonResponse(query_list, safe=False)

@login_required(login_url='login')
def scan_qr_create_view(request):
    form = scan_qr_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = scan_qr_form()

    context  = {
        'form': form
    }
    return render(request, "warehousedbapp/scan_qr.html", context)


# def scan_qr(request):
#     if request.method == 'GET':
#         context = {'form': scan_qr_form()}
#         return render(request,"warehousedbapp/scan_qr.html", context)
#     elif request.method == 'POST':
#         form = scan_qr_form(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             template = render(request, 'profile.html')
#             template['Hx-Push'] = '/profile/'
#             return template

#         ctx = {}
#         ctx.update(csrf(request))
#         form_html = render_crispy_form(form, context=ctx)
#         return HttpResponse(form_html)


# def info_from_qr(request, *args, **kwargs):
#     if kwargs.get('pk', None):
#         q = kwargs.get('pk', None)
#         queryset = warehouseadapp.objects.all().values('photo').filter(id = q) 
#         query_list = list(queryset)
#     # Decode QR-CODE into JSON
#         img_add = 'media/' + query_list[0]['photo']
#         image = cv2.imread(img_add)
#         barcodes = pyzbar.decode(image)
#         if barcodes:
#             qr_code = {'qr_decode': barcodes[0].data.decode('utf-8')}
#         else: qr_code = {'qr_decode': '0'}
#         query_list.append(qr_code)
#     # Decode weight numbers
#         # weight_reader_open_img =  Image.open(img_add)
#         # weight_reader_decode_img = pytesseract.image_to_string(weight_reader_open_img, config='--psm 6')
#         # if weight_reader_decode_img:
#         #     weight_decode = {'weight_decode': weight_reader_decode_img.replace("\n", "").replace("\f", "")}
#         # else: weight_decode = {'weight_decode': 0}
#         # query_list.append(weight_decode)
#     return JsonResponse(query_list, safe=False)