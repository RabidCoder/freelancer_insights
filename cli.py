from core.query_parser import handle_query


while True:
    a = input()
    if a in ['exit', 'выход']:
        break
    handle_query(a)