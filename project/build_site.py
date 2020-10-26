"""
CSC1-141
description: project 1
author: Quincy Myles Jr.
"""

import build


def make_plan(text):
    """
    creates a data structure with a file given
    :param text: a file
    :return: a data structure
    """
    site = build.Website("", "", "", "", "", [])
    f = open(text)
    title = f.readline()
    site.title = title
    new_p = None
    para_list = []

    for line in f:
        line = line.strip()
        if len(line) == 0:
            para_list.append(new_p)
        elif line == "!new_paragraph":
            new_p = build.Paragraphs("", "", [])
        elif line[0:6] == "!title":
            new_p.title = line[7:]
        elif line[0:6] == "!image":
            split = line[7:].split(" ")
            image_name = split[0]
            image_width = "100%"
            if len(split) == 2:
                image_width = split[1]

            img = build.Images(image_name, image_width)
            new_p.image.append(img)
        else:
            new_p.text += line + "\n"
    site.body = para_list
    f.close()
    return site


def inputs(webs):
    """
    prompts the user for style
    :param webs: website data structure
    :return: website data structure
    """
    print("Background Color")
    webs.back_color = build.color()
    print("You will now choose a font")
    webs.font = build.font()
    print("Paragraph Text Color")
    webs.text_color = build.color()
    print("Heading Color")
    webs.head_color = build.color()
    return webs


def create(text):
    """
    creates a structure from input along with a file
    :param text: a file
    :return: a data structure
    """
    return inputs(make_plan(text))
