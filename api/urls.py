from django.urls import path,include
from . import views

urlpatterns = [
    path("addProduct/",view=views.addProduct,name="addProduct"),
    path("getProduct/",view=views.getProduct,name="getProduct"),
    path("getLatestProduct/",view=views.getLatestProduct,name="getLatestProduct"),
    path("getHotProduct/",view=views.getHotProduct,name="getHotProduct"),
    path("getProductDetails/",view=views.getProductDetails,name="getProductDetails"),
    path("getDraft/",view=views.getDraft,name="getDraft"),
    path("addDraft/",view=views.addDraft,name="addDraft"),
    path("addLatest/",view=views.addLatest,name="addLatest"),
    path("removeLatest/",view=views.removeLatest,name="removeLatest"),
    path("addHot/",view=views.addHot,name="addHot"),
    path("removeHot/",view=views.removeHot,name="removeHot"),
    path("addDeleted/",view=views.addDeleted,name="addDeleted"),
    path("restoreDeleted/",view=views.restoreDeleted,name="restoreDeleted"),
    path("getDeleted/",view=views.getDeleted,name="getDeleted"),
    path("getLiveProduct/",view=views.getLiveProduct,name="getLiveProduct"),
    path("loginUser/",view=views.loginUser,name="loginUser"), 
    path("getInquiry/",view=views.getInquiry,name="getInquiry"),
    path("addInquiry/",view=views.addInquiry,name="addInquiry"),
    path("addImageSlider/",view=views.addImageSlider,name="addImageSlider"),
    path("getImageSlider/",view=views.getImageSlider,name="getImageSlider"),
    path("convert_csv/",view=views.convert_csv,name="convert_csv"),
   
]
