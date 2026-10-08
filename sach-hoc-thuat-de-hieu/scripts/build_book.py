#!/usr/bin/env python3
"""Dựng sách từ Markdown ra 3 file: .tex, .pdf (XeLaTeX) và .docx (pandoc).

Cách dùng:
    python3 build_book.py <thư_mục_sách> [--out <thư_mục_ra>] [--name <tên_file>]

Thư mục sách cần có:
    book.yaml      — thông tin bìa (xem assets/book.yaml mẫu)
    chapters.txt   — danh sách file .md theo thứ tự, mỗi dòng một file
    *.md           — nội dung
    img/           — hình minh hoạ (PNG)
"""
import argparse, os, shutil, subprocess, sys, yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")

ap = argparse.ArgumentParser()
ap.add_argument("book")
ap.add_argument("--out", default=None)
ap.add_argument("--name", default="sach")
a = ap.parse_args()

book = os.path.abspath(a.book)
out = os.path.abspath(a.out or os.path.join(book, "build"))
os.makedirs(out, exist_ok=True)
env = dict(os.environ, LANG="C.UTF-8", LC_ALL="C.UTF-8")   # BẮT BUỘC: tránh lỗi mã hoá tiếng Việt

meta = yaml.safe_load(open(os.path.join(book, "book.yaml"), encoding="utf8"))
files = [l.strip() for l in open(os.path.join(book, "chapters.txt"), encoding="utf8")
         if l.strip() and not l.startswith("#")]

def tex_escape(t):
    return (str(t).replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%")
            .replace("#", r"\#").replace("_", r"\_"))

# 1) Macro cho bìa và tiêu đề trang (đặt TRƯỚC header.tex)
vars_tex = os.path.join(out, "vars.tex")
with open(vars_tex, "w", encoding="utf8") as f:
    for key, macro in [("title_line1", "bookTitleA"), ("title_line2", "bookTitleB"),
                       ("title_line3", "bookTitleC"), ("subtitle", "bookSubtitle"),
                       ("tagline", "bookTagline"), ("footer", "bookFooter"),
                       ("running_head", "bookRunningHead")]:
        f.write("\\newcommand{\\%s}{%s}\n" % (macro, tex_escape(meta.get(key, ""))))
    cover = meta.get("cover_image", "")
    f.write("\\def\\bookCover{%s}\n" % cover)   # dùng \def (không dùng newcommand) để \ifx so sánh được với \empty

# 2) Metadata cho docx (file YAML để giữ đúng UTF-8)
meta_docx = os.path.join(out, "meta_docx.yaml")
full_title = " ".join(str(meta.get(k, "")) for k in ("title_line1", "title_line2", "title_line3")).strip()
with open(meta_docx, "w", encoding="utf8") as f:
    yaml.safe_dump({"title": meta.get("docx_title", full_title),
                    "subtitle": meta.get("subtitle", ""),
                    "toc-title": "Mục lục", "lang": "vi-VN"}, f, allow_unicode=True,
                   explicit_start=True, explicit_end=False)
    f.write("---\n")

src = [os.path.join(book, x) for x in files]
filt = os.path.join(HERE, "filter.lua")
common = ["-f", "markdown+pipe_tables+fenced_divs+tex_math_dollars", "--lua-filter", filt,
          "--number-sections", "--toc", "--toc-depth=1", "--highlight-style=tango"]

# 3) LaTeX
tex = os.path.join(out, a.name + ".tex")
subprocess.run(["pandoc", *src, "-o", tex, "--standalone", "--top-level-division=chapter", *common,
                "-H", vars_tex, "-H", os.path.join(ASSETS, "header.tex"),
                "-B", os.path.join(ASSETS, "titlepage.tex"),
                "-V", "documentclass=book", "-V", "classoption=openany", "-V", "fontsize=11pt",
                "-V", "fontfamily=fontspec",          # tránh lỗi thiếu lmodern.sty với XeLaTeX
                "-V", "lang=vi", "-V", "colorlinks=true", "-V", "linkcolor=cdark",
                "-V", "urlcolor=cblue", "-V", "toccolor=black",
                "-M", "pdftitle=" + full_title], check=True, env=env, cwd=book)

# 4) PDF (chạy 2 lần để mục lục đúng số trang)
img_link = os.path.join(out, "img")
if not os.path.exists(img_link):
    os.symlink(os.path.join(book, "img"), img_link)
for _ in range(2):
    subprocess.run(["xelatex", "-interaction=nonstopmode", os.path.basename(tex)],
                   cwd=out, env=env, stdout=subprocess.DEVNULL)

# 5) DOCX
ref = os.path.join(out, "reference.docx")
subprocess.run([sys.executable, os.path.join(HERE, "make_reference_docx.py"), ref], check=True, env=env)
docx = os.path.join(out, a.name + ".docx")
subprocess.run(["pandoc", meta_docx, *src, "-o", docx, *common, "--reference-doc", ref,
                "--resource-path", book], check=True, env=env, cwd=book)

# 6) Báo cáo
log = open(os.path.join(out, a.name + ".log"), encoding="utf8", errors="ignore").read()
missing = sorted({l.strip()[:90] for l in log.splitlines() if "Missing character" in l})
errors = [l for l in log.splitlines() if l.startswith("!")]
print("PDF :", os.path.join(out, a.name + ".pdf"))
print("DOCX:", docx)
print("TEX :", tex)
print("Lỗi LaTeX:", len(errors)); [print("  ", e) for e in errors[:10]]
print("Ký tự thiếu phông:", len(missing)); [print("  ", m) for m in missing[:15]]
