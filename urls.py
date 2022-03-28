from datetime import date
from views import Index, Contact, Another_page, Page, Examples


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/contact/': Contact(),
    '/another_page/': Another_page(),
    '/page/': Page(),
    '/examples/': Examples(),

}