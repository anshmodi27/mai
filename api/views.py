from django.shortcuts import render, HttpResponse, redirect
import json
from django.core import serializers
from django.contrib.auth.models import User 
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import (
    Product,Category,Inquiry,ImageSlider)
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
@csrf_exempt
def addProduct(request):
    if request.method == "POST":
        productName = request.POST.get("productname")
        category= request.POST.get("category")
        packaging = request.POST.get("packaging")
        description= request.POST.get("description")
        image= request.FILES.get("image")
        

        product = Product.objects.filter(productName=productName)
        if product:
            path=request.POST.get("path")
            product = Product.objects.get(productName=productName)
            product.productName = productName
            product.productLink= (
                    productName.replace(" ", "-").replace("--", "").replace("---", "")
                   )
            product.crop = category
            product.packing = packaging
            product.description = description
            if(image):
                product.images = image
            else:    
                product.images = path
            product.listdes = json.loads(description)
            
            product.category = Category.objects.get(categoryName=category)
            product.isLive = True
            product.save()
            return HttpResponse(
            json.dumps({"msg": "Your details Updated successfully."}),
            content_type="application/json",
            )   
        else:
            newproduct = Product()
            newproduct.productName = productName
            newproduct.productLink= (
                    productName.replace(" ", "-").replace("--", "").replace("---", "")
                   )
            newproduct.crop = category
            newproduct.packing = packaging
            newproduct.description = description
            newproduct.listdes = json.loads(description)
            newproduct.images = image
            newproduct.category = Category.objects.get(categoryName=category)
            newproduct.isLive = True
            newproduct.save()
            return HttpResponse(
            json.dumps({"msg": "Your details saved successfully."}),
            content_type="application/json",
            )

@csrf_exempt
def addDraft(request):
    if request.method == "POST":
        productName = request.POST.get("productname")
        category= request.POST.get("category")
        packaging = request.POST.get("packaging")
        description= request.POST.get("description")
        image= request.FILES.get("image")
        
        if productName:
        
            newproduct = Product()
            newproduct.productName = productName
            newproduct.productLink= (
                    productName.replace(" ", "-").replace("--", "").replace("---", "")
                )
            newproduct.crop = category
            newproduct.packing = packaging
            newproduct.description = description
            newproduct.images = image
            newproduct.category = Category.objects.get(categoryName=category)
            newproduct.isLive = False
            newproduct.save()
            return HttpResponse(
            json.dumps({"msg": "Your details drafted successfully."}),
            content_type="application/json",
            )
        return HttpResponse(
            json.dumps({"msg": "Plese enter product name To Save Draft."}),
            content_type="application/json",
            )
                

       
@csrf_exempt
def getProductDetails(request):
    if request.method == "GET":
        product = request.GET.get("product")
        products_data = Product.objects.filter(productLink=product).first()
        product_serialized = serializers.serialize("json", [products_data])
        return HttpResponse(product_serialized, content_type="application/json")
    
@csrf_exempt
def getProduct(request):
    if request.method == "GET":
        products = Product.objects.filter(isLive=True,isDeleted=False).all()
        products_data = serializers.serialize("json", products)
        return HttpResponse(products_data, content_type="application/json") 
    
@csrf_exempt
def getLiveProduct(request):
    if request.method == "GET":
        products = Product.objects.filter(isLive=True,isDeleted=False).all()
        products_data = serializers.serialize("json", products)
        return HttpResponse(products_data, content_type="application/json")     

@csrf_exempt
def getDraft(request):
    if request.method == "GET":
        products = Product.objects.filter(isLive=False).all()
        products_data = serializers.serialize("json", products)
        return HttpResponse(products_data, content_type="application/json")         
    
@csrf_exempt
def getDeleted(request):
    if request.method == "GET":
        products = Product.objects.filter(isDeleted=True).all()
        products_data = serializers.serialize("json", products)
        return HttpResponse(products_data, content_type="application/json")             
        
@csrf_exempt
def getHotProduct(request):
    if request.method == "GET":
        products = Product.objects.filter(isHot=True).all()
        products_data = serializers.serialize("json", products)
        return HttpResponse(products_data, content_type="application/json")     
    
@csrf_exempt
def getLatestProduct(request):
    if request.method == "GET":
        products = Product.objects.filter(isLatest=True).all()
        products_data = serializers.serialize("json", products)
        return HttpResponse(products_data, content_type="application/json")     
    

@csrf_exempt
def addLatest(request):
    if request.method == "GET":
        product = request.GET.get("product")
        products = Product.objects.filter(productLink=product)
        if products:
            products=Product.objects.get(productLink=product)
            products.isLatest=True
            products.save()
            return HttpResponse(
        json.dumps({"msg": "product add in latest category successfully."}),
        content_type="application/json",
        )
        return HttpResponse(
        json.dumps({"msg": "something went wrong."}),
        content_type="application/json",
        )  
    
@csrf_exempt
def addDeleted(request):
    if request.method == "GET":
        product = request.GET.get("product")
        products = Product.objects.filter(productLink=product)
        if products:
            products=Product.objects.get(productLink=product)
            products.isDeleted=True
            products.save()
            return HttpResponse(
        json.dumps({"msg": "product deleted successfully."}),
        content_type="application/json",
        )
        return HttpResponse(
        json.dumps({"msg": "something went wrong."}),
        content_type="application/json",
        )   

@csrf_exempt
def restoreDeleted(request):
    if request.method == "GET":
        product = request.GET.get("product")
        products = Product.objects.filter(productLink=product)
        if products:
            products=Product.objects.get(productLink=product)
            products.isDeleted=False
            products.save()
            return HttpResponse(
        json.dumps({"msg": "product restored successfully."}),
        content_type="application/json",
        )
        return HttpResponse(
        json.dumps({"msg": "something went wrong."}),
        content_type="application/json",
        )     


@csrf_exempt
def removeLatest(request):
    if request.method == "GET":
        product = request.GET.get("product")
        products = Product.objects.filter(productLink=product)
        if products:
            products=Product.objects.get(productLink=product)
            products.isLatest=False
            products.save()
            return HttpResponse(
        json.dumps({"msg": "product remove in latest category successfully."}),
        content_type="application/json",
        )
        return HttpResponse(
        json.dumps({"msg": "something went wrong."}),
        content_type="application/json",
        ) 

@csrf_exempt
def addHot(request):
    if request.method == "GET":
        product = request.GET.get("product")
        products = Product.objects.filter(productLink=product)
        if products:
            products=Product.objects.get(productLink=product)
            products.isHot=True
            products.save()
            return HttpResponse(
        json.dumps({"msg": "product add in Hot category  successfully."}),
        content_type="application/json",
        )
        return HttpResponse(
        json.dumps({"msg": "something went wrong."}),
        content_type="application/json",
        )  
@csrf_exempt
def removeHot(request):
    if request.method == "GET":
        product = request.GET.get("product")
        products = Product.objects.filter(productLink=product)
        if products:
            products=Product.objects.get(productLink=product)
            products.isHot=False
            products.save()
            return HttpResponse(
        json.dumps({"msg": "product remove in Hot category  successfully."}),
        content_type="application/json",
        )
        return HttpResponse(
        json.dumps({"msg": "something went wrong."}),
        content_type="application/json",
        )           
    
@csrf_exempt
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")

        
        user = authenticate( username=username, password=password)

        if user:
            
            login(request, user)

            
            return JsonResponse({
                "msg": "Login successful.",
                "user_id": user.id,
                "username": user.username,
            })
        else:
            return JsonResponse({"msg": "Invalid credentials."})
    else:
        return JsonResponse({"msg": "Invalid request method."})     

@csrf_exempt
def addInquiry(request):
    if request.method == "POST":
        fName = request.POST.get("firstname")
        category= request.POST.get("category")
        lname = request.POST.get("lastname")
        description= request.POST.get("description")
        email = request.POST.get("email")
        contect = request.POST.get("contact")
        selectedProduct = request.POST.get("selectedproduct")
        

        
        newInquiry = Inquiry()
        newInquiry.firstName=fName
        newInquiry.lastName=lname
        newInquiry.category=category
        newInquiry.email=email
        newInquiry.contectno=contect
        newInquiry.selected_product=selectedProduct
        newInquiry.selected_category=category
        newInquiry.description=description
        
        newInquiry.save()
        # Send email 
        subject = 'MAI Conformation'
        message = f'Thank you for submitting your details, {newInquiry.firstName + newInquiry.lastName}.\n\n'
        message += f'Client Name: {newInquiry.firstName + newInquiry.lastName}\n'
        message += f'Mobile No: {newInquiry.contectno}\n'
        message += f'selected category: {newInquiry.selected_category}\n'
        message += f'Email: {newInquiry.email}\n'
        message += f'selected product: {newInquiry.selected_product}\n\n'
        message += 'Please find attached PDF.'

        from_email = settings.EMAIL_HOST_USER  # Replace with your email
        to_email = [newInquiry.email,"missionagriindiapvtltd@gmail.com"]

        email_message = EmailMessage(subject, message, from_email, to_email)
        

        try:
            email_message.send()
        except Exception as e:
            print(f"Error sending email: {e}")
        return HttpResponse(
        json.dumps({"msg": "Your request sent successfully. We will get back to you."}),
        content_type="application/json",
        )
    

@csrf_exempt
def getInquiry(request):
    if request.method == "GET":
        inquiry = Inquiry.objects.all().order_by('date')
        inquiry_data = serializers.serialize("json", inquiry)
        return HttpResponse(inquiry_data, content_type="application/json") 

                 
    
@csrf_exempt
def addImageSlider(request):
    if request.method == "POST":
        img1= request.FILES.get("image1")
        img2= request.FILES.get("image2")
        img3= request.FILES.get("image3")
        print(img1,img2,img3)
           

        obj = ImageSlider.objects.get(id=1)
        if img1 :
          if img1 != "":            
            with open(
                "/var/www/mai/media/slider/" + str(1) + ".jpg", "wb+"
            ) as destination:
                for chunk in img1.chunks():
                    destination.write(chunk)
                    
        if img2 :
          if img2 != "":
            with open(
                "/var/www/mai/media/slider/" + str(2) + ".jpg", "wb+"
            ) as destination:
                for chunk in img2.chunks():
                    destination.write(chunk)

        if img3 :
            if img3 != "":
                with open(
                    "/var/www/mai/media/slider/" + str(3) + ".jpg", "wb+"
                ) as destination:
                    for chunk in img3.chunks():
                        destination.write(chunk)            

        obj.image1="slider/" + str(1) + ".jpg" if img1 else ""
        obj.image2="slider/" + str(2) + ".jpg" if img2 else ""
        obj.image3="slider/" + str(3) + ".jpg" if img3 else ""
        obj.save()
        return HttpResponse(
        json.dumps({"msg": "images updated successfully"}),
        content_type="application/json",
        )    
    
@csrf_exempt
def getImageSlider(request):
    if request.method == "GET":    
      images = ImageSlider.objects.filter(id=1)
      images_serializers = serializers.serialize("json", images)
      return HttpResponse(images_serializers, content_type="application/json")   
    
import csv,os
from datetime import datetime, timedelta

# Function to filter inquiries based on a time interval
def filter_inquiries_by_interval(inquiries, interval):
    today = datetime.now()
    
    if interval == 'one_month':
        start_date = today - timedelta(days=30)
    elif interval == 'two_months':
        start_date = today - timedelta(days=60)
    elif interval == 'one_year':
        start_date = today - timedelta(days=365)
    else:
        # Handle unknown interval
        return inquiries

    return inquiries.filter(date__gte=start_date)

# Function to create a CSV file
def create_csv(inquiries, filename):
    media_root = settings.MEDIA_ROOT
    file_path = os.path.join(media_root, 'csv', filename)

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'firstName', 'lastName', 'contectno', 'email', 'selected_category', 'selected_product', 'date', 'time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for inquiry in inquiries:
            writer.writerow({
                'id': inquiry.id,
                'firstName': inquiry.firstName,
                'lastName': inquiry.lastName,
                'contectno': inquiry.contectno,
                'email': inquiry.email,
                'selected_category': inquiry.selected_category,
                'selected_product': inquiry.selected_product,
                'date': inquiry.date,
                'time': inquiry.time,
            })

def convert_csv(request):
    if request.method == "GET":
        

        inquiries = Inquiry.objects.all().order_by('date')
       
        create_csv(inquiries, 'inquires.csv')
        return JsonResponse({"filepath": "media/csv/inquires.csv"})
       

@csrf_exempt
def dbDownload(request):
    if request.user.is_superuser:
        # copy the database file to the static folder
        os.system("cp db.sqlite3 static/")
        return HttpResponse("<a href='/static/db.sqlite3' download>Download</a>")
