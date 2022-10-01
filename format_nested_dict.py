import ast


def format_item(item):
    if isinstance(item, str):
        try:
            item = ast.literal_eval(item)
            return format_item(item)
        except:
            return item

    elif isinstance(item, dict):
        d = dict()
        for k, v in item.items():
            d2 = format_item(v)
            d.update({k: d2})
        return d

    elif isinstance(item, list):
        l = list()
        for i in range(len(item)):
            s = format_item(item[i])
            l.append(s)
        return l

    elif isinstance(item, bool):
        if item:
            return 'true'
        else:
            return 'false'

    elif item is None:
        return 'null'

    else:
        return item
