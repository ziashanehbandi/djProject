# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from .models import articles
#
# # def home(request):
# #     return HttpResponse('this is home page')
# #
# # def about(request):
# #     return HttpResponse('this is about-us page')
# #
# # def name(request):
# #     return JsonResponse({
# #         1:{'name': 'zia',
# #            'age':20
# #            },
# #         2:{'name': 'k',
# #            'age':20
# #            },
# #         3:{'name': 'zia',
# #            'age':30
# #            }
# #     })
#
# def html(request):
#     context={
#         'articles':articles.objects.all()
#
#         # 'articles':[
#         # {
#         # 'title':'عکس فوری آخرین یاغی فوتبال ایران با پیراهن آبی',
#         # 'img':'https://static.farakav.com/files/pictures/thumb/01587244.jpg',
#         # 'describtion':'آرمان رمضانی شب گذشته برای دقایقی کوتاه با لباس استقلال به میدان رفت ولی فرصت چندانی برای درخشش پیدا نکرد.'
#         # },
#         # {
#         # 'articles':'مانوئل نویر؛ خیاطی و دوخت و دوز در اوج حساسیت!',
#         # 'img':'https://static.farakav.com/files/pictures/thumb/01587224.jpg',
#         # 'describtion':'در پیروزی 1-0 بایرن مونیخ برابر لایپزیش در شب گذشته نویر بازی را با تلاش برای دوختن تور دروازه خود آغاز کرد و با یک کلین شیت به پایان رساند.'
#         # }]
#     }
#     return render(request,'djangoProject/test.html',context)