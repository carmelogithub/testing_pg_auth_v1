from django.http import JsonResponse
import  aiohttp, asyncio
import time, requests

# sync view
def sync_api_view(request):
    start = time.time()
    resp1 = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    resp2 = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()
    resp3 = requests.get('https://jsonplaceholder.typicode.com/users/1').json()
    return JsonResponse({'data': [resp1, resp2, resp3], 'execution_time': time.time() - start})

# async view usando asyncio y aiohttp
async def async_api_view(request):
    start = time.time()
    async def fetch(url):
        async with aiohttp.ClientSession() as s:
            async with s.get(url) as r:
                return await r.json()
    results = await asyncio.gather(
        fetch('https://jsonplaceholder.typicode.com/todos/1'),
        fetch('https://jsonplaceholder.typicode.com/posts/1'),
        fetch('https://jsonplaceholder.typicode.com/users/1'),
    )
    return JsonResponse({'data': results, 'execution_time': time.time() - start})