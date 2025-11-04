# Python Static Site Generator
This repository contains a small static site generator written in Python.
It’s a personal project designed to work for me and my needs. If you think it might work for you too, I encourage you to clone this repo and experiment.

There's no how-to guide at the moment since it's mainly a personal project. However, I plan to include a simple setup guide down the road.

# Overview
A simple static site generator built with python and minimal dependencies. It's designed to do one thing -- generate a blog.

The generator converts `.md` files with YAML front matter into static HTML pages, applies a standard boilerplate with a link to a global stylesheet, and outputs a complete static site.

Designed around a clear and minimal folder layout:
```
input/            → Source markdown posts  
output/           → Generated HTML output  
output/assets/    → CSS, fonts, images
```

# Dependencies
- [markdown-it-py](https://pypi.org/project/markdown-it-py/) — parses markdown and YAML frontmatter, converts to HTML
- [pillow](https://pypi.org/project/pillow/) — resizes images to lighten the load

# Environment
This project uses [uv](https://docs.astral.sh/uv/) to manage dependencies and the Python environment.
