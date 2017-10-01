from urllib.parse import parse_qs


def application(env, start_response):
    html = """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>%(title)s</title>
    </head>
    <body>
        <p>%(text)s</p>
    </body>
    </html>
    """
    query_params = parse_qs(env['QUERY_STRING'])
    response_body = html % {
        'text': generate_page_text(query_params),
        'title': generate_page_title(env['PATH_INFO']),
    }
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),

    ]
    start_response(status, response_headers)
    return [response_body.encode('utf8')]


def generate_page_text(query_params):
    result_text = ''
    if not query_params:
        result_text = 'Я хочу увидеть параметры запроса!!'
    else:
        for key in query_params:
            result_text += '<p>Я вижу параметр "'+\
                           key+'", его значение равняется "'+\
                           query_params[key][0]+'"</p>'
    return result_text


def generate_page_title(path_info):
    routes_map = {
        '/': 'Это главная страница',
        '/about': 'Это страница "О нас"'
    }
    title = 'Я не знаю о такой странице, попробуйте ещё раз'
    for key in routes_map:
        if path_info == key or path_info == key+'/':
            title = routes_map[key]
    return title
