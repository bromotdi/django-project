from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization # кроме аутентификация выполняем и авторизацию пользователя 
from .authentication import CustomAuthentication

class CategotyResourse(ModelResource): # расширяем импортированный класс ModelResource
    class Meta: # собственный атрибут класса
        queryset = Category.objects.all() # все категории с бд
        resource_name = 'categories' # путь к получению доступа к api-сервера
        allowed_methods = ['get'] # разрешение только на чтение категорий, методы post, set, delete недоступны
      
      
class CourseResourse(ModelResource): 
    class Meta:
        queryset = Course.objects.all() 
        resource_name = 'courses' 
        allowed_methods = ['get', 'post', 'delete'] 
        excludes = ['reviews_qty', 'created_at'] # поля, которые хотим исключить 
        authentication = CustomAuthentication()
        authorization = Authorization()
        
    def hydrate(self, bundle): #обработка данных от клиента
        bundle.obj.category_id = bundle.data['category_id']
        return bundle
    
    def dehydrate(self, bundle): #влияет на то, как данные возращаються клиенту
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle
    
    def dehydrate_title(self, bundle): #влияет на то, как данные возращаються клиенту
        return bundle.data['title'].upper()
    