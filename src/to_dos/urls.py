
from .views import todo_detail_view, todo_list_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),

]
