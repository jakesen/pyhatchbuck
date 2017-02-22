class ApiObject(object):

    def __init__(self, json_data=None):
        if json_data != None:
            self.load_dict(json_data)
        self.__initialised = True

    def load_dict(self, json_data):
        for k, v in json_data.iteritems():
            if hasattr(self, k):
                object_attr = getattr(self, k, None)
                if isinstance(object_attr, ApiObjectList):
                    setattr(self, k, ApiObjectList(object_attr.object_class, v))
                elif isinstance(object_attr, ApiStringAttribute):
                    setattr(self, k, ApiStringAttribute(v))
                elif isinstance(object_attr, ApiIntegerAttribute):
                    setattr(self, k, ApiIntegerAttribute(v))
                elif isinstance(object_attr, ApiBooleanAttribute):
                    setattr(self, k, v)
                elif isinstance(object_attr, ApiObject):
                    setattr(self, k, type(object_attr)(v))

    def as_dict(self):
        output = {}
        for key in self.__class__.__dict__.keys():
            object_attr = getattr(self, key)
            value = None
            if isinstance(object_attr, ApiObjectList):
                value = object_attr.as_dict_list()
            elif isinstance(object_attr, ApiStringAttribute):
                value = str(object_attr)
            elif isinstance(object_attr, ApiIntegerAttribute):
                value = int(object_attr)
            elif isinstance(object_attr, ApiObject):
                value = object_attr.as_dict()
            if value not in ('', [], {}, None):
                output[key] = value
        return output

    def __setattr__(self, name, value):
        if self.__dict__.has_key('_ApiObject__initialised'):
            object_attr = getattr(self, name, None)
            if isinstance(object_attr, ApiObjectList) and not isinstance(value, ApiObjectList):
                super(ApiObject, self).__setattr__(name, ApiObjectList(value))
            elif isinstance(object_attr, ApiStringAttribute) and not isinstance(value, ApiStringAttribute):
                super(ApiObject, self).__setattr__(name, ApiStringAttribute(value))
            elif isinstance(object_attr, ApiIntegerAttribute) and not isinstance(value, ApiIntegerAttribute):
                super(ApiObject, self).__setattr__(name, ApiIntegerAttribute(value))
            elif isinstance(object_attr, ApiObject) and not isinstance(value, ApiObject):
                super(ApiObject, self).__setattr__(name, ApiObject(value))
            else:
                super(ApiObject, self).__setattr__(name, value)
        else:
            super(ApiObject, self).__setattr__(name, value)


class ApiStringAttribute(str):

    def __init__(self, value=None):
        super(ApiStringAttribute, self).__init__(value)

class ApiIntegerAttribute(int):

    def __init__(self, value=None):
        super(ApiIntegerAttribute, self).__init__(value)

class ApiBooleanAttribute(object):
    pass

class ApiObjectList(list):

    def __init__(self, object_class, json_list=None):
        self.object_class = object_class
        if json_list:
            super(ApiObjectList, self).__init__([object_class(i) for i in json_list])

    def as_dict_list(self):
        return [object_instance.as_dict() for object_instance in self]
