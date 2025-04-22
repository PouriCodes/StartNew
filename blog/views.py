from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, "blog/blog-home.html")

def blog_single(request):
    context = {
        'title': 'Forex Trading',
        'content': 'This is the content of the blog forex page.',
        'author': 'Pouria N',
        'date': '2025-11-07',
    }
    return render(request, "blog/blog-single.html",context)
