import datetime
def date_in_future(integer=None):
    if isinstance(integer, int):
        result= datetime.datetime.now() + datetime.timedelta(days=integer)
        return result.strftime("%Y-%m-%d %H:%M:%S")        
    else:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(date_in_future(5))