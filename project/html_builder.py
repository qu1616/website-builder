"""
CSC1-141
description: project 1
author: Quincy Myles Jr.
"""

import sys
import build
import build_site


def user_input():
    """
    Prompts the user for inputs
    :return: website data structure
    """
    website_title = input("What is the title of your website? ")
    print("Background Color")
    back_color = build.color()
    print("You will now choose a font")
    style = build.font()
    print("Paragraph Text Color")
    text_color = build.color()
    print("Heading Color")
    head_color = build.color()
    body = build.paragraphs()

    return build.Website(website_title, back_color, style, text_color, head_color, body)


def build_body(p):
    """
    Creates the body for the site
    :param p: paragraphs
    :return: the body
    """
    out_body = ""
    for para in p:
        out_body += "<h2>" + para.title + "</h2>\n"
        out_body += "<p align= center>" + para.text + "</p>\n"
        image = para.image
        for image in para.image:
            out_body += "<img src=\"" + image.name + "\" width=\"" + image.width + "\" alt=\"pic\" class=\"center\" >\n"
    return out_body


def build_html(web, filename):
    """
    creates the html code
    :param web: website data structure
    :param filename: the file being created
    :return: an html page
    """
    f = open(filename, "w")
    f.write("""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {background-image: linear-gradient(180deg,""")

    f.write(web.back_color)
    f.write(""", white);}
            .center {
                display: block;
                margin-left: auto;
                margin-right: auto;
                }
            h1   {color:""")
    f.write(web.head_color)
    f.write(""";\n      font-family:""")
    f.write(web.font)
    f.write(""";
               text-align:center;
                  }

            h2   {color: """)
    f.write(web.head_color)
    f.write(""";
                  font-family: """)
    f.write(web.font)
    f.write(""";
                  text-align: justify;
                  }

            p    {color:""")
    f.write(web.text_color)
    f.write("""";
                  font-family: """)
    f.write(web.font)
    f.write(""";;
                  padding: 30px;
                  text-align: justify;
                  background-color: white;
                  box-shadow: 4px 0 2px -2px rgba(0,0,0,0.4);
                  font-size: 14px;
                  }

        </style>
        </head>
        <body>""")

    if len(sys.argv) > 1:
        f.write(build.build_link(sys.argv))
    f.write("<h1>" + web.title + "<h1>\n")
    f.write(build_body(web.body))
    f.write("</body>")
    f.write("</html>")
    print("Your file has been saved as index.html!")


def main():
    """
    Calls either wizard or website mode
    :return: an html page
    """
    # wizard mode
    if len(sys.argv) == 1:
        build_html(user_input(), "index.html")
    else:
        # website mode
        for file in sys.argv[1:]:
            build_html(build_site.create(file), file.replace(".txt", ".html"))


main()
