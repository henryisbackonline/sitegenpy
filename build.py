#!/usr/bin/env python3
import os
import shutil
import argparse
from markdown_it import MarkdownIt

# --- Configuration ---
INPUT_DIR = "input"
OUTPUT_DIR = os.path.join("site", "Posts")

def build_site():
    """Converts Markdown files in input/ into HTML pages in site/Posts/."""
    if not os.path.exists(INPUT_DIR):
        print(f"❌ Input folder '{INPUT_DIR}' not found.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    md_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".md")]

    if not md_files:
        print("⚠️ No markdown files found in input/.")
        return

    md = MarkdownIt()

    for filename in md_files:
        input_path = os.path.join(INPUT_DIR, filename)
        base_name = os.path.splitext(filename)[0]

        # Derive folder name: capitalize and replace underscores with spaces
        post_title = base_name.replace("_", " ").title()
        output_folder = os.path.join(OUTPUT_DIR, post_title)
        os.makedirs(output_folder, exist_ok=True)

        output_html = os.path.join(output_folder, "post.html")

        # Read and convert markdown
        with open(input_path, "r", encoding="utf-8") as f:
            markdown_content = f.read()
        html_content = md.render(markdown_content)

        # Wrap in minimal HTML
        html_page = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{post_title}</title>
        </head>
        <body>
        <main>
        {html_content}
        </main>
        </body>
        </html>
        """

        # Write HTML file
        with open(output_html, "w", encoding="utf-8") as f:
            f.write(html_page)

        # Copy attachments if they exist
        attachments_src = os.path.join(INPUT_DIR, "attachments")
        attachments_dest = os.path.join(output_folder, "attachments")

        if os.path.exists(attachments_src):
            if os.path.exists(attachments_dest):
                shutil.rmtree(attachments_dest)
            shutil.copytree(attachments_src, attachments_dest)
            print(f"📸 Copied attachments for {post_title}")

        print(f"✅ Built: {output_html}")

    print("\n🎉 Build complete! Output available in /site/Posts/")

def main():
    parser = argparse.ArgumentParser(description="Simple Markdown → HTML site builder")
    parser.add_argument("--build", action="store_true", help="Build the static site")
    args = parser.parse_args()

    if args.build:
        build_site()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()