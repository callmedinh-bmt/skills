#!/usr/bin/env python3
"""Kiểm tra chất lượng bản thảo TRƯỚC khi dựng, và ảnh xem trước SAU khi dựng.

    python3 check_book.py <thư_mục_sách> [--lang java] [--forbid "10 tuổi" "cho bé"]
    python3 check_book.py <thư_mục_sách> --preview build/sach.pdf --pages 1-12

Kiểm tra:
  1. Hình được nhắc tới có tồn tại trong img/ không
  2. Emoji / ký tự ngoài vùng phông (sẽ thành ô trống trong PDF)
  3. Cụm từ bị cấm (ví dụ cách xưng hô người dùng không muốn)
  4. Code block không đúng ngôn ngữ đã chọn (--lang)
  5. Tên kiểu snake_case trong backtick khi ngôn ngữ là Java/C#/Kotlin/JS
  6. Mỗi chương (# ...) có ít nhất 1 hình và 1 hộp bài tập
"""
import argparse, glob, os, re, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument("book")
ap.add_argument("--lang", default=None, help="ngôn ngữ code chính, ví dụ java / python")
ap.add_argument("--allow-lang", nargs="*", default=["json", "yaml", "sql", "bash", "text", "mermaid"],
                help="ngôn ngữ phụ được phép (khi ngôn ngữ chính không phù hợp)")
ap.add_argument("--forbid", nargs="*", default=[])
ap.add_argument("--preview", default=None, help="file PDF để xuất ảnh xem trước")
ap.add_argument("--pages", default="1-12")
a = ap.parse_args()

book = os.path.abspath(a.book)
order = os.path.join(book, "chapters.txt")
files = ([l.strip() for l in open(order, encoding="utf8") if l.strip() and not l.startswith("#")]
         if os.path.exists(order) else sorted(os.path.basename(f) for f in glob.glob(os.path.join(book, "*.md"))))
problems = 0
in_appendix = False   # sau khối ::: {.appendix} thì không đòi hình/bài tập

def warn(msg):
    global problems
    problems += 1
    print("  ✗", msg)

EMOJI = re.compile("[\U0001F000-\U0001FFFF\u2600-\u26FF\u2700-\u27BF]")
ALLOWED_SYMBOLS = set("★✗")      # đã được map phông trong header.tex
CAMEL_LANGS = {"java", "kotlin", "csharp", "cs", "javascript", "js", "typescript", "ts", "go", "swift"}

for fn in files:
    t = open(os.path.join(book, fn), encoding="utf8").read()
    print(f"[{fn}]")
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', t):
        if not os.path.exists(os.path.join(book, m.group(1))):
            warn(f"thiếu hình: {m.group(1)}")
    for ch in set(EMOJI.findall(t)) - ALLOWED_SYMBOLS:
        warn(f"ký tự có thể không hiển thị trong PDF: {ch!r} (U+{ord(ch):04X})")
    for phrase in a.forbid:
        for m in re.finditer(re.escape(phrase), t, re.I):
            line = t.count("\n", 0, m.start()) + 1
            warn(f"cụm từ bị cấm '{phrase}' ở dòng {line}")
    if a.lang:
        for m in re.finditer(r'^```(\w*)', t, re.M):
            lang = m.group(1)
            if lang and lang != a.lang and lang not in a.allow_lang:
                line = t.count("\n", 0, m.start()) + 1
                warn(f"code block '{lang}' ở dòng {line} (ngôn ngữ chính là {a.lang})")
        if a.lang in CAMEL_LANGS:
            prose = re.sub(r'```.*?```', '', t, flags=re.S)
            for m in re.finditer(r'`([a-z]+_[a-z0-9_]+)(\([^`]*\))?`', prose):
                warn(f"tên kiểu snake_case trong văn bản: `{m.group(0)}` — đổi sang camelCase cho khớp {a.lang}")
    if in_appendix:
        continue
    body = t
    if "{.appendix}" in t:
        body = t.split("{.appendix}")[0]
        in_appendix = True
    chapters = re.split(r'^# (?!#)', body, flags=re.M)[1:]
    for c in chapters:
        title = c.splitlines()[0]
        if "unnumbered" in title:
            continue
        if "![" not in c:
            warn(f"chương '{title[:50]}' chưa có hình minh hoạ")
        if 'kind="ex"' not in c:
            warn(f"chương '{title[:50]}' chưa có hộp bài tập")

print(f"\nTổng cộng: {problems} vấn đề")

if a.preview:
    first, last = a.pages.split("-")
    outdir = os.path.join(os.path.dirname(os.path.abspath(a.preview)), "preview")
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(["pdftoppm", "-jpeg", "-r", "45", "-f", first, "-l", last, a.preview,
                    os.path.join(outdir, "p")], check=True)
    from PIL import Image
    ims = [Image.open(f) for f in sorted(glob.glob(os.path.join(outdir, "p-*.jpg")))]
    w, h = ims[0].size
    cols = 6
    sheet = Image.new("RGB", (cols * w, ((len(ims) + cols - 1) // cols) * h), "white")
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * w, (i // cols) * h))
    p = os.path.join(outdir, "pages.jpg")
    sheet.save(p, quality=75)
    print("Ảnh xem trước:", p)
