import yaml
from collections import OrderedDict


class YamlOp(object):

    def __init__(self, file, stream=None):
        self.file = file
        self.stream = stream
        self.info = self.ordered_yaml_load()

    def ordered_yaml_load(self, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
        class OrderedLoader(Loader):
            pass

        def construct_mapping(loader, node):
            loader.flatten_mapping(node)
            return object_pairs_hook(loader.construct_pairs(node))

        OrderedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)

        if self.stream:
            return yaml.load(self.stream, OrderedLoader)
        with open(self.file, 'r') as stream:
            return yaml.load(stream, OrderedLoader)

    @classmethod
    def ordered_yaml_dump(cls, data, file=None, stream=None, Dumper=yaml.SafeDumper, **kwds):
        class OrderedDumper(Dumper):
            pass

        def _dict_representer(dumper, data):
            return dumper.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())

        OrderedDumper.add_representer(OrderedDict, _dict_representer)
        output = yaml.dump(data, stream, OrderedDumper, **kwds)
        with open(file, 'w') as f:
            f.write(output)