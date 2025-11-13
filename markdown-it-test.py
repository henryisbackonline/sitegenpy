# =============================================================================================== #
# FROM THE markdown-it-py docs

# from markdown_it import MarkdownIt
# from mdit_py_plugins.front_matter import front_matter_plugin
# from mdit_py_plugins.footnote import footnote_plugin

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

# a | b
# - | -
# 1 | 2

# A footnote [^1]

# [^1]: some details
# """)
# print(md.render(text))

# =============================================================================================== #
# TESTING FILE READ AND WRITE

# from markdown_it import MarkdownIt

# md = MarkdownIt()

# with open ('testfile.md', 'r', encoding='utf-8') as f:
#     markdown_text = f.read()

# html_output = md.render(markdown_text)

# with open ('testfile.html', 'w', encoding='utf-8') as f:
#     f.write(html_output)

# =============================================================================================== #
# TESTING MARKDOWN FRONTMATTER READING

from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
import yaml # need yaml actually parse and render the yaml data - frontmatter plugin only seperates it from the markdown file

md = MarkdownIt().use(front_matter_plugin)

frontmatter = {} # create an empty dictionary to store the frontmatter in

def get_frontmatter(md, fm_text):
    "passes the string retieved by front_matter_plugin to pyyaml and adds it to the frontmatter dict"
    global frontmatter
    frontmatter = yaml.safe_load(fm_text)

md.options["put_frontmatter"] = get_frontmatter

with open ('testfile.md', 'r', encoding='utf-8') as file:
    markdown_text = file.read()

html_output = md.render(markdown_text)

with open ('testfile.html', 'w', encoding='utf-8') as file:
    file.write(html_output)