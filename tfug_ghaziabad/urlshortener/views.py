from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import URL

def redirect_view(request, code):
    url_instance = get_object_or_404(URL, short_code=code)
    return HttpResponse(f"""
        <html>
            <head>
                <meta http-equiv="refresh" content="0;url={url_instance.original_url}" />
                <script type="text/javascript">
                    window.location.href = '{url_instance.original_url}';
                </script>
            </head>
            <body>
                <p>If you are not redirected automatically, follow this <a href="{url_instance.original_url}">link</a>.</p>
            </body>
        </html>
    """)

def urlshortner(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        url_instance = URL(original_url=original_url)
        url_instance.save()
        short_url = url_instance.tfug_url
    else:
        short_url = None
    
    urls = URL.objects.all()
    return render(request, 'urlshortner.html', {'short_url': short_url, 'urls': urls})