excluded_attrs = ['name', 'tag_type', 'body']


def get_tag_pair(tag):
    tag_name = tag["name"]
    tag_body = tag["body"]
    result = f'<{tag_name}'
    for key in tag:
        if key not in excluded_attrs:
            result += f' {key}="{tag[key]}"'
    return result + f'>{tag_body}</{tag_name}>'


def get_tag_single(tag):
    result = f'<{tag["name"]}'
    for key in tag:
        if key not in excluded_attrs:
            result += f' {key}="{tag[key]}"'
    return result + ">"


tags_mapping = {
    "pair": get_tag_pair,
    "single": get_tag_single,
}


def error_message(*args, **kwargs):
    return "Error: Invalid language"


def stringify(tag):
    tag_type = tag["tag_type"]
    if tag_type == "pair":
        func = tags_mapping.get(tag_type, error_message)
    elif tag_type == "single":
        func = tags_mapping.get(tag_type, error_message)
    else:
        return error_message()

    return func(tag)


#  мой первый вариант
# def get_tag_pair(tag):
#     tag_name = tag["name"]
#     tag_body = tag["body"]
#     result = f'<{tag_name}'
#     for key in tag:
#         if key in ["name", "tag_type", "body"]:
#             continue
#         else:
#             result += f' {key}="{tag[key]}"'
#     result += f'>{tag_body}</{tag_name}>'
#     return result
#     # '<p>text</p>'
#     # '<div id="wow">text2</div>'
#     # '<div id="wow" way="value">text2</div>'


# def get_tag_single(tag):
#     result = f'<{tag["name"]}'
#     for key in tag:
#         if key in ["name", "tag_type"]:
#             continue
#         result += f' {key}="{tag[key]}"'
#     return result + ">"
#     # expected = '<hr class="px-3" id="myid">'


# def error_message(*args, **kwargs):
#     return "Error: Invalid language"


# tags_mapping = {
#     "pair": get_tag_pair,
#     "single": get_tag_single,
# }


# def stringify(tag):
#     tag_type = tag["tag_type"]
#     if tag_type == "pair":
#         func = tags_mapping.get(tag_type, error_message)
#     elif tag_type == "single":
#         func = tags_mapping.get(tag_type, error_message)
#     else:
#         return error_message()

#     return func(tag)


# !решение ментора
# ?BEGIN (write your solution here)
# excluded_attrs = ['name', 'tag_type', 'body']


# def build_attrs(tag):
#     acc = []
#     for attr in tag:
#         if attr not in excluded_attrs:
#             acc.append(f' {attr}="{tag[attr]}"')
#     return ''.join(acc)


# mapping = {
#     'single': lambda tag: f"<{tag['name']}{build_attrs(tag)}>",
#     'pair': lambda tag: f"<{tag['name']}{build_attrs(tag)}>{tag['body']}</{tag['name']}>",  # noqa: E501
# }


# def stringify(tag):
#     build = mapping[tag['tag_type']]
#     return build(tag)
# ?END
