#ProfeSearch

Busca a tus profesores antes de llegar al salón.

##Idea

Este app te permite hacer search de los profesores de diferentes universidades de Puerto Rico. Es una aplicación sencilla que se alimenta del REST API de [Notaso](https://notaso.com).  La idea principal de esta aplicación es que funcione como ejemplo para los desarrolladores, para que vean y tengan una idea de como implementar el REST API de Notaso en sus aplicaciones. 

Para desarrollar esta aplicación utilicé:
* [Django-AngularJS](https://github.com/jrief/django-angular.git)
* Notaso [REST API](https://notaso.com/api/) - [Docs](https://notaso.com/docs/)

##Instalar

```bash
$ git clone https://github.com/luisjorge129/ProfeSearch.git
$ cp .env.example .env
$ pip install -r requirements.txt
$ python manage.py runserver
```

Abre tu browser en [http://localhost:8000/](http://localhost:8000/).
