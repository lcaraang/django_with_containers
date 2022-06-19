from django.urls import path
from .import views

app_name = 'posts' # allows using 'posts:index' for url and reverse_lazy methods
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('publish/<int:pk>', views.publish, name='publish'),
    path('ordered', views.OrderedView.as_view(), name='ordered'),
    path('filtered', views.FilteredView.as_view(), name='filtered'),
    path('filtered-ordered', views.FilteredOrderedView.as_view(), name='filtered-ordered'),
    
]
