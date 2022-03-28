from simba_framework.templator import render


def context(request):
    return {'date': request.get('date', None), 'year': request.get('year', None)}


class Index:
    def __call__(self, request):
        data = context(request)
        data['title'] = 'Index'
        return '200 OK', render('index.html', data=data)


class Contact:
    def __call__(self, request):
        data = context(request)
        data['title'] = 'Contact'
        return '200 OK', render('contact.html', data=data)


class Another_page:
    def __call__(self, request):
        data = context(request)
        data['title'] = 'Another_page'
        return '200 OK', render('another_page.html', data=data)


class Examples:
    def __call__(self, request):
        data = context(request)
        data['title'] = 'Examples'
        return '200 OK', render('examples.html', data=data)


class Page:
    def __call__(self, request):
        data = context(request)
        data['title'] = 'Page'
        return '200 OK', render('page.html', data=data)