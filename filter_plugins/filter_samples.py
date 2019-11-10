

def filter_samples(actual, sample):
    res = {}
    for entry in actual:
        if entry in sample['System']:
            res[entry] = sample['System'][entry]
    return res

class FilterModule(object):
    ''' param_list_compare '''

    def filters(self):
        return {
            'filter_samples': filter_samples
        }
