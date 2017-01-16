class ApiObject(object):

    def __init__(self, json_data=None):
        if json_data:
            for k, v in json_data.iteritems():
                if hasattr(self, k):
                    object_attr = getattr(self, k, None)
                    if isinstance(object_attr, ApiObjectList):
                        setattr(self, k, ApiObjectList(object_attr.object_class, v))
                    elif isinstance(object_attr, ApiStringAttribute):
                        setattr(self, k, ApiStringAttribute(v))
                    elif isinstance(object_attr, ApiListAttribute):
                        setattr(self, k, ApiListAttribute(v))
                    elif isinstance(object_attr, ApiBooleanAttribute):
                        setattr(self, k, v)
                    elif isinstance(object_attr, ApiObject):
                        setattr(self, k, type(object_attr)(v))

class ApiStringAttribute(str):

    def __init__(self, value=None):
        super(ApiStringAttribute, self).__init__(value)

class ApiListAttribute(list):

    def __init__(self, value=[]):
        super(ApiListAttribute, self).__init__(value)

class ApiBooleanAttribute(object):
    pass

class ApiObjectList(list):

    def __init__(self, object_class, json_list=None):
        self.object_class = object_class
        if json_list:
            super(ApiObjectList, self).__init__([object_class(i) for i in json_list])
