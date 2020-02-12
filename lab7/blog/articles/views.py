from django.shortcuts import render

# Create your views here.
from articles.models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
        # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
        # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
        # если поля заполнены без ошибок
                if form["title"] in list(map(lambda x: x.title,Article.objects.all())):
                    # проверка уникальности статьи
                    form['errors'] = u"Данная статься уже существует, попробуйте другое название"
                    return render(request, 'create_post.html', {'form': form})
                else:
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
            # перейти на страницу поста
            else:
        # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})

    else:
        raise Http404
def registration(request):
    if request.method == "POST":
        form = {
                'login': request.POST["login"],
                'password': request.POST["password"],
                'email':request.POST["email"]
            }
        if form["login"] and form["password"] and form["email"]:
            try:
                User.objects.get(username=form['login'])
                # если пользователь существует, то ошибки не произойдет и программа # удачно доберется до следующей строчки 
                form['errors'] = u"Данный пользователь существует"
                return render(request, 'registration.html', {'form': form})
            except User.DoesNotExist:
                User.objects.create_user(form["login"], form["email"], form["password"])
                form['errors'] =  u"Пользователь {0} успешно создан".format(form["login"])
                return render(request, 'registration.html', {'form': form})
        else:
            form['errors'] =  u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})

    else:
        return render(request, 'registration.html', {})
def auth(request):
    if request.method == "POST":
        form = {
                'login': request.POST["login"],
                'password': request.POST["password"],
            }
        if form["login"] and form["password"]:
            user = authenticate(username=form['login'], password=form['password'])
            if user:
                login(request, user)
                form['errors'] = u"Вы успешно авторизировались"
                return render(request, 'auth.html', {'form': form})
            else:
                form['errors'] = u"Данного пользователя не существует"
                return render(request, 'auth.html', {'form': form})
        else:
            form['errors'] =  u"Не все поля заполнены"
            return render(request, 'auth.html', {'form': form})

    else:
        return render(request, 'auth.html', {})
