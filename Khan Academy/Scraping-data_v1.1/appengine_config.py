from gaesessions import SessionMiddleware

COOKIE_KEY='12345678901234567890123456789012345'
def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = SessionMiddleware(app, cookie_key=COOKIE_KEY)
    app = recording.appstats_wsgi_middleware(app)
    return app
