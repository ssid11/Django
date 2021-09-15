from django.shortcuts import render

# Create your views here.
def index(request):
    content = {'title':'geekshop start page'}
    return render(request,'mainapp/index.html',content)

def products(request):
    PRODUCT_DIR = 'vendor/img/products/'
    content = {'products':
                   [{'name':'Худи черного цвета с монограммами adidas Originals',
                     'price':6090,
                     'desc':'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                     'img':PRODUCT_DIR + 'Adidas-hoodie.png',},

                    {'name': 'Синяя куртка The North Face',
                     'price':23725,
                    'desc': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                    'img':PRODUCT_DIR + 'Blue-jacket-The-North-Face.png',},

                    {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                     'price':3390,
                     'desc': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                     'img':PRODUCT_DIR + 'Brown-sports-oversized-top-ASOS-DESIGN.png',},

                    {'name': 'Черный рюкзак Nike Heritage',
                      'price': 2340,
                      'desc': 'Плотная ткань. Легкий материал.',
                      'img': PRODUCT_DIR + 'Black-Nike-Heritage-backpack.png', },

                     {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                      'price': 13590,
                      'desc': 'Гладкий кожаный верх. Натуральный материал.',
                      'img': PRODUCT_DIR + 'Black-Dr-Martens-shoes.png', },

                     {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                      'price': 2890,
                      'desc': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                      'img': PRODUCT_DIR + 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', },
                    ]
            }
    return render(request,'mainapp/products.html',content)
