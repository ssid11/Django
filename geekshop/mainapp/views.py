from django.shortcuts import render

# Create your views here.
def index(request):
    content = {'title':'geekshop start page'}
    return render(request,'mainapp/index.html',content)

def products(request):
    content = {'products':
                   [{'name':'Худи черного цвета с монограммами adidas Originals',
                     'price':6090,
                     'desc':'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                     'img':'/static/vendor/img/products/Adidas-hoodie.png',},
                    {'name': 'Синяя куртка The North Face',
                     'price':23725,
                    'desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                    'img':'/static/vendor/img/products/Blue-jacket-The-North-Face.png',},
                    {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                     'price':3390,
                     'desc': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                     'img':'/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',},
                    ]
            }
    return render(request,'mainapp/products.html',content)
