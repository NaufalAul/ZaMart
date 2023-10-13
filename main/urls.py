from django.urls import path
from main.views import add_product_ajax, delete_product_ajax, get_product_json, show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_item, reduce_item,  delete_item, edit_product


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('add_item/<int:product_id>', add_item, name='add_item'),
    path('reduce_item/<int:product_id>', reduce_item, name='reduce_item'),
    path('delete_item/<int:product_id>', delete_item, name='delete_item'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'), 
    path('delete-product-ajax/', delete_product_ajax, name='delete_product_ajax')
]