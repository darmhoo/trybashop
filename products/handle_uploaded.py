def handle(f):
    with open('img/2018/07/23/dami2.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)