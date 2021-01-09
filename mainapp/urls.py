from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('application/',add_data, name='g'),
    path('application/',add_data,name='application'),
    path('dashboard/',dashboard, name='dashboard'),
    path('about/',about, name='about'),
    path('services/',services, name='services'),
    path('contact/',contact, name='contact'),
    path('thanks/',thanks, name='thanks'),
    
    path('products/<user_id>', ProductListView.as_view(), name='products'),
    path('products/category/<user_id>', ProductCategoryListView.as_view(), name='product-category-view'),
    path('products/category/<user_id>/new', ProductCategoryCreateView.as_view(), name='add-product-category'),
    path('products/category/<int:pk>/update', ProductCategoryUpdateView.as_view(), name='category-edit'),
    path('products/category/<int:pk>/delete', ProductCategoryDeleteView.as_view(), name='category-delete'),
    path('products/new/', ProductCreateView.as_view(), name='add-product'),
    path('products/<int:pk>/detail', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('products/<user_id>/production-volume', ProductionVolumeCreateView.as_view(), name='edit-product'),
    
    path('accounts/register/',signup,name='register'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='mainapp/login.html'),name='login'),
    path('accounts/logout/',auth_views.LogoutView.as_view(template_name='mainapp/home.html'),name='logout'),
    path('user/firm/',user_firm_create_form,name='user-firm'),
    
    path('sales/order/create',sales_order_create_form,name='sales-order-create'),
    path('sales/order/<int:pk>/update',sales_order_edit_form,name='sales-order-edit'),
    path('sales/order/<user_id>', SalesOrderListView.as_view(), name='sales-order-view'),
    path('sales/order/<int:pk>/view', SalesOrderDetailView.as_view(), name='sales-order-details'),
    path('sales/order/<int:pk>/delete', SalesOrderDeleteView.as_view(), name='sales-order-delete'),
    
    path('purchase/order/create',purchase_order_create_form,name='purchase-order-create'),
    path('purchase/order/<int:pk>/update',purchase_order_edit_form,name='purchase-order-edit'),
    path('purchase/order/<user_id>', PurchaseOrderListView.as_view(), name='purchase-order-view'),
    path('purchase/order/<int:pk>/view', PurchaseOrderDetailView.as_view(), name='purchase-order-details'),
    path('purchase/order/<int:pk>/delete', PurchaseOrderDeleteView.as_view(), name='purchase-order-delete'),
    
    path('machines/<user_id>', MachineListView.as_view(), name='machine-list'),
    path('machines/<user_id>/create', MachineCreateView.as_view(), name='machine-create'),
    path('machines/<int:pk>/update', MachineUpdateView.as_view(), name='machine-edit'),
    path('machines/<int:pk>/detail', MachineDetailView.as_view(), name='machine-detail'),
    path('machines/<int:pk>/delete', MachineDeleteView.as_view(), name='machine-delete'),
    
    path('machines/maintenance/<user_id>', MaintenanceListView.as_view(), name='maintenance-list'),
    path('machines/maintenance/<user_id>/new', MaintenanceCreateView.as_view(), name='maintenance-create'),
    path('machines/maintenance/<int:pk>/update', MaintenanceUpdateView.as_view(), name='maintenance-edit'),
    path('machines/maintenance/<int:pk>/delete', MaintenanceDeleteView.as_view(), name='maintenance-delete'),

    # not being used now
    path('update_employee/', update_employee, name='update_employee'),
    path('add_employee/', add_employee, name='add_employee'),
    path('edit_employee/<str:pk>/', edit_employee, name='edit_employee'),
    path('create_designation/', create_designation, name='create_designation'),
    
    path('customers/<user_id>',CustomerListView.as_view(),name='customer-list'),
    path('customers/<user_id>/create',CustomerCreateView.as_view(),name='customer-create'),
    path('customers/<int:pk>/update',CustomerUpdateView.as_view(),name='customer-edit'),
    path('customers/<int:pk>/delete',CustomerDeleteView.as_view(),name='customer-delete'),
    path('customers/<int:pk>/view',CustomerDetailView.as_view(),name='customer-detail'),
    path('vendors/<user_id>',VendorListView.as_view(),name='vendor-list'),
    path('vendors/<user_id>/create',VendorCreateView.as_view(),name='vendor-create'),
    path('vendors/<int:pk>/update',VendorUpdateView.as_view(),name='vendor-edit'),
    path('vendors/<int:pk>/delete',VendorDeleteView.as_view(),name='vendor-delete'),
    path('vendors/<int:pk>/view',VendorDetailView.as_view(),name='vendor-detail'),
    path(r'updatechart/', solver),
    
]