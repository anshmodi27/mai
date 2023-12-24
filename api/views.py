from django.shortcuts import render, HttpResponse, redirect
import json
from django.core import serializers
from django.contrib.auth.models import User 
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import (
    Product,Category,Inquiry)

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
