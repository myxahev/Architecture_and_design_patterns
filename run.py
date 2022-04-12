from wsgiref.simple_server import make_server
from simba_framework.main import Framework, FakeApplication
from urls import fronts
from views import routes

application = Framework(routes, fronts)

with make_server('', 8090, application) as httpd:
    print("Запуск на порту 8090...")
    httpd.serve_forever()
