def get_links(tags):
    return [
        tag.get("href") if tag["name"] in ["a", "link"] else
        tag.get("src") if tag["name"] == "img" else None
        for tag in tags
        if tag["name"] in ["a", "link", "img"]
    ]

#  мой первый вариант
# def get_links(tags):
#     result = []
#     for tag in tags:
#         if tag["name"] in ["a", "link"]:
#             result.append(tag.get("href"))
#         elif tag["name"] in ["img"]:
#             result.append(tag.get("src"))
#         else:
#             continue
#     return result


# !решение ментора
# ?BEGIN (write your solution here)
# \\MAPPING = {
# \\    'a': 'href',
# \\    'img': 'src',
# \\    'link': 'href',
# \\}


# \\def get_links(tags):
# \\    result = []
# \\    for tag in tags:
# \\      name = tag['name']
# \\      if name in MAPPING:
# \\          attr = MAPPING[tag['name']]
# \\          result.append(tag[attr])
# \\  return result
# END
