from django.urls import path
# Импортируем созданные нами представления
from .views import ProductsList, ProductDetail,create_product


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
 # Для этого вызываем метод as_view.
   path('', ProductsList.as_view()),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', ProductDetail.as_view()),#Product верно  так как получить хотим 1 товар
# Для этого вызываем метод as_view.
#path('', ProductsList.as_view()),
   path('create/', create_product, name = 'product_crete'),

]

