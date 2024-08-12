from django.urls import path
from . import views

urlpatterns = [
path('',views.index, name='home'),
path('login/',views.login_view,name='login'),
path('register/',views.register_view,name='register'),
path('todo/<int:id>/delete',views.delete_func,name='todo_delete'),
path('todo/<int:id>/toggle',views.toggle,name='todo_toggle')
]



# / 
# /products - список продуктов
# /products/123 - информация о продукте с id 123
# /products/437/edit
# /products/437/delete
# /products/create

# /products/category/74 - продукты из категории 74
# /products/category/74/edit 






# /products/page/3 - отобразить продукты страница 3 
