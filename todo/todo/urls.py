from django.conf.urls import patterns, include, url
from todo.addtodo.views import TodoView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^v1/todos/?$', TodoView.as_view()),
)
