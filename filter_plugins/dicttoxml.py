from lxml import etree

def dicttoxml(data, root):
    r = etree.Element(root)
    return etree.tostring(buildxml(r, data)).decode('utf-8')

def buildxml(element, data, prev=None):
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, dict):
                child = etree.Element(k)
                buildxml(child, v)
                element.append(child)
            elif isinstance(v, (list, tuple)):
                for item in v:
                    child = etree.Element(k)
                    buildxml(child, item, k)
                    element.append(child)
            else:
                child = etree.Element(k)
                if v is None:
                    element.append(child)
                else:
                    child.text = str(v)
                    element.append(child)
    elif isinstance(data, (list, tuple)):
        for item in v:
            child = etree.Element(prev)
            buildxml(child, v)
            element.append(child)
    else:
        if data is not None:
            element.text = str(data)
    return element


class FilterModule(object):
    ''' param_list_compare '''

    def filters(self):
        return {
            'dicttoxml': dicttoxml
        }
