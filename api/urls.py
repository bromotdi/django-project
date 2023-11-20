from api.models import CategotyResourse, CourseResourse
from tastypie.api import Api # c модуля api пакета tastipie импортируем класс Api
from django.urls import path, include

api = Api(api_name = 'v1') # экземпляр класса API c именем пути /v1
api.register(CategotyResourse()) #регистрируем ресурсы 
api.register(CourseResourse())

urlpatterns = [
    path('', include(api.urls), name = 'index')
]
