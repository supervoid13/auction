from django.urls import path
from lot import views

urlpatterns = [
    path('', views.lots_view, name='lots_page'),
    path(r'create/', views.LotCreateView.as_view(), name='create_lot'),
    path(r'<int:pk>/', views.specific_lot_view, name='lot_page'),
    path(r'<int:pk>/comment/', views.create_lot_comment, name='create_comment'),
    path(r'<int:lot_id>/edit', views.LotEditView.as_view(), name='edit_lot'),
    path(r'<int:lot_id>/add_to_favorites', views.add_to_favorites, name='add_to_favorites'),
    path(r'<int:lot_id>/remove_from_favorites', views.remove_from_favorites, name='remove_from_favorites'),
    path(r'<int:lot_id>/offer_price', views.raise_price, name='offer_price'),
]
