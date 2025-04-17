from django.http import HttpResponse,JsonResponse

def test_v(request):
    return HttpResponse("<h1>Hello, this is a test response from the view.</h1>")
# This is a simple Django view function that returns a plain text response.

def test_json(request):
    data = {
        "message": "Hello, this is a test response in JSON format.",
        "status": "success"
    }
    return JsonResponse(data)