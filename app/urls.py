from django.urls import path,re_path
from.import views
urlpatterns = [
    path('',views.SignUpView.as_view(),name='signup'),
    path('login/',views.LogInView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('books/',views.BookListView.as_view(),name='book_list_view'),
    path('update/<int:id>/',views.BookUpdateView.as_view(),name='update'),
    path('delete/<int:id>/',views.BookDeleteView.as_view(),name='delete'),
    path('book_detail/<int:pk>/',views.BookDetailView.as_view(),name='book_detail'),
    re_path(r'^.*/$', views.Custom404View.as_view(),name='custom_404'),
]
