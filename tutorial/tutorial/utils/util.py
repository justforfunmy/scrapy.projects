def parseCookies(str):
    str_list = str.split(';')
    cookie_obj = {}
    for item in str_list:
        item_l = item.split('=')
        cookie_obj[item_l[0]]=item_l[1]
    return cookie_obj