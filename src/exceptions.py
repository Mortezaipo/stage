class ConfigKeyNotFound(Exception):
    _level = "high"
    _message = "Key \"{}\" not found in config file."

    def __init__(self, key_name):
        super(ConfigKeyNotFound, self).__init__(self._message.format(key_name))


class ConfigSectionNotFound(Exception):
    _level = "high"
    _message = "Section \"{}\" not found in config file."

    def __init__(self, section_name):
        super(ConfigSectionNotFound, self).__init__(self._message.format(section_name))
