from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('cross_off/<item_id>', views.cross_off, name='cross_off'),
    path('uncross/<item_id>', views.uncross, name='uncross'),
    path('edit/<item_id>', views.edit, name='edit'),
]