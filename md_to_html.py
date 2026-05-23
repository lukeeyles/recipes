import markdown
import os

md = markdown.Markdown(extensions=['markdown.extensions.tables','meta'])
metadata = []
links = []

# write recipe posts
fns = os.listdir("md")
for fn in fns:
    name = fn.split(".")[0]
    link = "post/"+name+".html"
    with open(link,"w") as html_file, open("md/"+fn,"r") as md_file, open("template/recipe_header.html","r") as header_template, open("template/footer.html") as footer_template:
        html = md.convert(md_file.read())
        html = header_template.read() + html + footer_template.read()
        html_file.write(html)
        md.Meta["url"] = [link]
        metadata.append(md.Meta)

# write index page with list of posts
with open("index.html","w") as html_file, open("template/header.html","r") as header_template, open("template/footer.html") as footer_template:
    html = ""
    for item in metadata:
        html += f"<p><a href={item["url"][0]}>{item["title"][0]}</a> {item["date"][0]}</p>\n"
    html = header_template.read() + html + footer_template.read()
    html_file.write(html)