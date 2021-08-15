import jsonpath


class MyDict(dict):
    def __getattr__(self, item):
        value = self.get(item)
        if type(value) == dict:
            value = MyDict(value)
        if isinstance(value, list) or isinstance(value, tuple):
            value = list(value)
            for index, v in enumerate(value):
                if isinstance(v, dict):
                    value[index] = MyDict(v)
        return value


def get_dict_value(dic, field, one=True):
    json_path = "$..%s" % field
    data = jsonpath.jsonpath(dic, json_path)
    if not data:
        return
    if one:
        return data[0]
    return data
