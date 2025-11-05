from markdown_it import MarkdownIT

md = MarkdownIt()
md.render("example string with *italics* and **bold** and `code`.")