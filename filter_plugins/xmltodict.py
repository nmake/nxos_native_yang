from lxml import etree

def xmltodict(string):
    xml = etree.XML(string)
    res = elem2dict(xml)
    return res

def elem2dict(node):
    """
    Convert an lxml.etree node tree into a dict.
    """
    result = {}

    for element in node.iterchildren():
        # Remove namespace prefix
        key = element.tag.split('}')[1] if '}' in element.tag else element.tag
        # Process element as tree element if the inner XML contains non-whitespace content
        if element.text and element.text.strip():
            value = element.text
        else:
            value = elem2dict(element)
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                tempvalue = result[key].copy()
                result[key] = [tempvalue, value]
        else:
            result[key] = value

    if result:
        return result
    else:
        return None

class FilterModule(object):
    ''' param_list_compare '''

    def filters(self):
        return {
            'xmltodict': xmltodict
        }
