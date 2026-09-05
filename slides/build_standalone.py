import base64, io, os, re, sys
root = r"C:\Users\victo\neurosymbolic-reasoning-shortcuts"
slides = os.path.join(root, "slides")
src = os.path.join(slides, "index.html")
html = io.open(src, encoding="utf-8").read()
original_len = len(html)

def read(rel):
    p = os.path.normpath(os.path.join(slides, rel))
    return io.open(p, encoding="utf-8").read()

# 1. inline stylesheets, preserving order
def css_sub(m):
    href = m.group(1)
    return "<style>\n/* inlined from %s */\n%s\n</style>" % (href, read(href))
html, n_css = re.subn(r'<link rel="stylesheet" href="(\.\./reveal\.js/[^"]+)"\s*/?>', css_sub, html)

# 2. inline scripts, preserving order
def js_sub(m):
    s = m.group(1)
    return "<script>\n/* inlined from %s */\n%s\n</script>" % (s, read(s))
html, n_js = re.subn(r'<script src="(\.\./reveal\.js/[^"]+)"></script>', js_sub, html)

# 3. inline images as data URIs
def img_sub(m):
    rel = m.group(1)
    p = os.path.normpath(os.path.join(slides, rel))
    b64 = base64.b64encode(open(p, "rb").read()).decode("ascii")
    return 'src="data:image/png;base64,%s"' % b64
html, n_img = re.subn(r'src="(assets/[^"]+\.png)"', img_sub, html)

out = os.path.join(slides, "deck-standalone.html")
io.open(out, "w", encoding="utf-8").write(html)
print("stylesheets inlined:", n_css)
print("scripts inlined    :", n_js)
print("images inlined     :", n_img)
print("remaining external refs:", len(re.findall(r'(?:href|src)="(?!https?:|#|data:)[^"]+"', html)))
print("output size: %.2f MB" % (os.path.getsize(out)/1048576))
print("index.html untouched:", len(io.open(src, encoding="utf-8").read()) == original_len)