# from markdown_it import MarkdownIt
# from mdit_py_plugins.front_matter import front_matter_plugin
# from mdit_py_plugins.footnote import footnote_plugin
# 
# md = (
#     MarkdownIt()
#     .use(front_matter_plugin)
#     .use(footnote_plugin)
#     .enable('table')
# )
# text = ("""\
# ---
# a: 1
# ---
# 
# a | b
# - | -
# 1 | 2
# 
# A footnote [^1]
# 
# [^1]: some details
# """)
# print(md.render(text))

from markdown_it import MarkdownIt

md = MarkdownIt()

with open ('testfile.md', 'r', encoding='utf-8') as f:
    markdown_text = f.read()

html_output = md.render(markdown_text)

with open ('testfile.hmlt', 'w', encoding='utf-8') as f:
    f.write(html_output)