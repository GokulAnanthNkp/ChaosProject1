import pip

def import_module(package):
    try:
        return __import__(package)
    except ImportError:
        pip.main(['install', package])
    #return __import__(package)

# Example
if __name__ == '__main__':
        test = import_module('chaostoolkit')
        test2 = import_module('chaostoolkit-aws')
        test3 = import_module('chaostoolkit-lib[jsonpath]')
        print(test3)
