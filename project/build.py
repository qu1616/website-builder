"""
CSC1- 141
description: project 1
author: Quincy Myles Jr.
"""


from dataclasses import dataclass
from typing import List
import turtle as t


@dataclass()
class Link:
    website: list
    files: list


@dataclass()
class Images:
    name: str
    width: str


@dataclass()
class Paragraphs:
    title: str
    text: str
    image: List[Images]


@dataclass()
class Website:
    title: str
    back_color: str
    font: str
    text_color: str
    head_color: str
    body: List[Paragraphs]


COLORS = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen', 'lawngreen',
          'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen', 'chocolate',
          'yellowgreen',
          'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred',
          'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred ', 'antiquewhite', 'royalblue', 'yellow',
          'indigo ', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki',
          'darkviolet',
          'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise', 'lightyellow', 'grey', 'whitesmoke', 'blueviolet',
          'orchid', 'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen', 'gainsboro', 'darkorange',
          'cornflowerblue',
          'lightsteelblue', 'plum', 'lavender', 'palegreen', 'darkred', 'dimgray', 'floralwhite', 'orangered',
          'oldlace',
          'darksalmon', 'lavenderblush', 'darkslategray', 'tan', 'cadetblue', 'silver', 'tomato', 'darkkhaki',
          'slategray',
          'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson', 'mistyrose', 'lime', 'saddlebrown',
          'blanchedalmond',
          'black', 'snow', 'seashell', 'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod', 'palevioletred', 'fuchsia',
          'teal',
          'lightpink', 'darkgrey', 'mediumspringgreen', 'aquamarine', 'lightsalmon', 'navajowhite', 'darkgreen',
          'burlywood',
          'rosybrown', 'springgreen', 'purple', 'olivedrab', 'lightslategrey', 'orange', 'aliceblue',
          'mediumaquamarine',
          'navy', 'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink', 'mediumpurple',
          'skyblue',
          'aqua', 'blue', 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise', 'brown', 'thistle',
          'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green', 'lightgoldenrodyellow', 'mediumturquoise',
          'steelblue',
          'lightgray', 'lightgrey', 'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite', 'dodgerblue',
          'greenyellow',
          'dimgrey', 'darkorchid'}

FONTSTYLE = {
    '0': 'Arial, size 14',
    '1': "Comic Sans MS, size 14",
    '2': "Lucida Grande, size 14",
    '3': "Tahoma, size 14",
    '4': "Verdana, size 14",
    '5': "Helvetica, size 14",
    '6': "Times New Roman, size 14"
}


def color():
    """
    error checks the color given
    :return: the color
    """
    name = input("Choose the name of a color, or in #XXXXXX: ")
    if name in COLORS:
        return name
    else:
        if name[0] is "#" and len(name) is 7:
            return name
        else:
            print("Not a valid color. Input a Correct color value.")
            return color()


def init():
    """
    sets up turtle
    :return: none
    """
    t.setup(200, 300)
    t.penup()
    t.left(180)
    t.forward(75)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.pendown()


def space():
    """
    creates a space between words
    :return: none
    """
    t.penup()
    t.right(90)
    t.forward(25)
    t.left(90)
    t.pendown()


def font_window():
    """
    creates a window with example text
    :return: none
    """
    init()
    t.write("Arial", font=("Arial", 14, "normal"))
    space()
    t.write("Comic Sans MS", font=("Comic Sans MS", 14, "normal"))
    space()
    t.write("Lucida Grande", font=("Lucida Grande", 14, "normal"))
    space()
    t.write("Tahoma", font=("Tohoma", 14, "normal"))
    space()
    t.write("Verdana", font=("Verdana", 14, "normal"))
    space()
    t.write("Helvetica", font=("Helvetica", 14, "normal"))
    space()
    t.write("Times New Roman", font=("Times New Roman", 14, "normal"))
    t.done()


def font():
    """
    gives a user a font option
    :return: font
    """
    f = input("Do you want to see what the font looks like? [yes/no] ")
    if f != "no":
        font_window()
    print(FONTSTYLE)
    num = input("Choose a font by its number ")
    if num in FONTSTYLE:
        return FONTSTYLE[num]
    else:
        print("Choose a valid style")
        return font()


def paragraph():
    """
    makes a single paragraph
    :return: paragraph structure
    """
    images = []
    title = input("Enter a title for your paragraph: ")
    content = input("Content of your paragraph: ")
    qu = input("Do you want to add an image?")
    while qu != "no":
        img = input("Image file name: ")
        images.append(Images(img, ''))
        qu = input("Do you want to add another image? ")
        if qu is "no":
            break
    return Paragraphs(title, content, images)


def paragraphs():
    """
    creates multiple paragraphs
    :return: a list of paragraphs
    """
    qu = input("Would you like to add a paragraph? ")
    paras = []
    while qu != "no":
        paras.append(paragraph())
        qu = input("Would you like to add another paragraph? ")
        if qu is "no":
            break
    return paras


def build_link(link: List[str]):
    """
    creates a link for an html page
    :param link: link from the sys
    :return: the written link code
    """
    temp = ''
    for file in link[1:]:
        html_file = file[:-3] + 'html'
        temp += "\n<p><a href=\"%s\">%s</a></p>" % (html_file, file)
    return temp
