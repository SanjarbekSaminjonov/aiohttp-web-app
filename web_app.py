from aiohttp import web
from aiohttp.web_fileresponse import FileResponse
from aiohttp.web_response import json_response


routes = web.RouteTableDef()

count = 0


@routes.get('/')
async def index(request):
    return FileResponse('static/index.html')


@routes.get('/get')
async def get_count(request):
    global count
    return json_response({
        'request': 'success',
        'count': count
    })


@routes.post('/add')
async def add_count(request):
    global count
    count += 1
    return json_response({
        'request': 'success',
        'count': count
    })
