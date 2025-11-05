# Python Static Site Generator
This repository contains a small static site generator written in Python.
It’s a personal project designed to work for me and my needs. If you think it might work for you too, I encourage you to clone this repo and experiment.

There's no how-to guide at the moment since it's mainly a personal project. However, I plan to include a simple setup guide down the road.

# Overview
A simple static site generator built with python and minimal dependencies. It's designed to do one thing - generate a blog.

The generator converts `.md` files with YAML front matter into static HTML pages, applies a standard boilerplate with a link to a global stylesheet, and outputs a complete static site.

Designed around a clear and minimal folder layout:
```
.
├── input/                # input folder for all markdown
└── output                # output folder for whole blog/
    ├── _assets/
    │   ├── fonts/
    │   ├── global/       # theme, boilerplate, favicons
    │   └── img/          # all images
    ├── about/
    ├── now/
    └── posts/            #html posts
```

# Dependencies
- [markdown-it-py](https://pypi.org/project/markdown-it-py/) — parses markdown and YAML frontmatter, converts to HTML
- [pillow](https://pypi.org/project/pillow/) — resizes images to lighten the load

# Environment
This project uses standard python tooling.

To get started:
- install [homebrew](brew.sh)
- install python (`brew install python`)
- alias python in zsh to make your life easier (`alias python='python3'`)
- run `python -m venv .venv` - this will create a virtual environment in the project root
- activate the venv with `source .venv/bin/activate`
  - the terminal should now be prefixed with `(.venv)`
- run `pip install markdown-it-py pillow`

That's it, everything is installed from scratch. If course, you could choose to install `pillow` and `markdown-it-py` systemwide withouth the `venv`, but i find this way a bit cleaner.
