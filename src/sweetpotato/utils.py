"""Functions for utils
"""

default_exports = {"@eva-design/eva": "* as eva"}
replace_attrs_dict = {
    "theme": {
        "dark": "{...eva.dark}",
        "light": "{...eva.light}",
    }
}
non_dict_attrs = ["...eva"]


def replace_attrs(attr, key):
    """
    Replaces attribute key/value with proper value.

    :param attr:
        str
    :param key:
        str
    :return:
        str
    """
    value = replace_attrs_dict[key][attr]
    is_dict = replace_attrs_dict[key][attr]
    attr = f"'{value}'" if replace_attrs_dict[key]["quotes"] else value
    attr = attr if not is_dict and attr else "{" + attr + "}"
    return attr


def format_attr_dict(attr, key=None):
    """
    Formats attribute dictionary to play nice with react-native.

    :param attr:
        str
    :param key:
        str | None
    :return:
        str
    """

    if key in replace_attrs_dict:
        attr = replace_attrs(attr, key)

    return attr if attr in default_exports.values() else "{" + str(attr) + "}"
