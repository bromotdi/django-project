from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication): #расширяем класс ApiKeyAuthentication, который отвечает на аунтефикацию по api-ключу
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET': #если у нас get запрос мы не делаем аунтефикацию пользователя
            return True
        else:
            return super().is_authenticated(request, **kwargs) #с помощью super временно создается экземпляр класса ApiKeyAuthentication и для него вызывается метод именно родительського класса is_authenticated