from pprint import pprint
from markdown_it import MarkdownIt

md = MarkdownIt()
md.render("example test. contains *italics* and **bold.**")