import asyncio
from django.shortcuts import redirect
from django.http import HttpResponse
from asyncio import sleep
import time

import httpx

async def home(request):
    start = time.time()
    await sleep(2)
    end = time.time()
    duration = end - start
    
    return redirect(f'timer/?duration={duration:.2f}')
    
def timer(request):
    duration = request.GET.get('duration')
    return HttpResponse(f'<h1>Tempo de execução: {duration}</h1><br><a href="/async_view">va para a pagina async</a>')

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse(f"<h1>Async view</h1> <br> <a href='/sync_view'>veja o sincrono</a>")

def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)

def sync_view(request):
    http_call_sync()
    return HttpResponse(f"<h1>Sync view</h1> <br> <a href='/async_view'>veja o assíncrono</a>")