from aiohttp import web

from web_app import routes


app = web.Application()
app.add_routes(routes=routes)
app.router.add_static(prefix='/static', path='static')

web.run_app(app=app, port='8000', host='localhost')
