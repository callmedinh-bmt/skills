#!/usr/bin/env python3
"""Thư viện nhỏ để vẽ sơ đồ minh hoạ đồng bộ phong cách cho sách.

Dùng Graphviz (sơ đồ khối, luồng, trạng thái) — nhanh, chữ tiếng Việt rõ nét.
Dùng Matplotlib (helper `mpl_save`) cho hình tự do: hình lồng nhau, toạ độ, bậc thang...

Ví dụ:
    from diagrams import dot, B, G, O, P, R, Y, GR
    dot("img/cache.png", f'''
      a [label="Máy chủ", {B}];
      c [label="Cache\\n(nhanh)", {O}];
      a -> c [label="1. hỏi cache"];
    ''', rankdir="LR")

QUY TẮC VÀNG
- Mỗi hình tối đa ~10 khối. Nhiều hơn thì tách thành 2 hình.
- Sơ đồ > 6 khối nối tiếp: dùng rankdir="TB" hoặc chia 2 hàng bằng {rank=same; ...}
  (sơ đồ quá rộng sẽ bị thu nhỏ, chữ không đọc được).
- Trong f-string, ngoặc nhọn của Graphviz phải viết đôi: {{rank=same; a; b;}}
- Màu có nghĩa: xanh dương = thành phần chính, xanh lá = kết quả tốt / lưu trữ,
  cam = bộ nhớ đệm / cảnh báo, tím = điều phối / AI, đỏ = lỗi / kiểm tra / nguy hiểm,
  vàng = người dùng / đầu vào, xám = bên ngoài / phụ.
- Nét đứt (style=dashed) = luồng phụ / trả về; nét chấm (dotted) = không đồng bộ.
- Không dùng emoji trong hình (phông không có).
"""
import subprocess, os

B  = 'fillcolor="#E8F1FB", color="#4A90D9"'   # xanh dương
G  = 'fillcolor="#E6F6EA", color="#3BA55C"'   # xanh lá
O  = 'fillcolor="#FFF1E0", color="#F08C00"'   # cam
P  = 'fillcolor="#F1E9FB", color="#8E5BD6"'   # tím
R  = 'fillcolor="#FDE8E8", color="#D64545"'   # đỏ
Y  = 'fillcolor="#FFF9DB", color="#C9A400"'   # vàng
GR = 'fillcolor="#F2F2F2", color="#888888"'   # xám

HEAD = '''digraph G {
  graph [fontname="DejaVu Sans", bgcolor="white", pad=0.3, nodesep=0.45, ranksep=0.55, dpi=200, rankdir=%s %s];
  node  [fontname="DejaVu Sans", fontsize=13, shape=box, style="rounded,filled",
         fillcolor="#E8F1FB", color="#4A90D9", penwidth=1.6, margin="0.18,0.10"];
  edge  [fontname="DejaVu Sans", fontsize=11, color="#555555", penwidth=1.3, arrowsize=0.8];
'''

def dot(path, body, rankdir="LR", extra=""):
    """Vẽ một sơ đồ Graphviz ra file PNG."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    src = HEAD % (rankdir, ("," + extra) if extra else "") + body + "\n}\n"
    r = subprocess.run(["dot", "-Tpng", "-o", path], input=src, text=True, capture_output=True)
    if r.returncode:
        raise RuntimeError(f"{path}: {r.stderr}")
    return path

def cluster(name, label, color, body):
    """Nhóm các khối vào một khung có tiêu đề."""
    return (f'subgraph cluster_{name} {{ label="{label}"; fontname="DejaVu Sans"; '
            f'color="{color}"; style=rounded;\n{body}\n}}')

def mpl_save(fig, path):
    """Lưu hình matplotlib với cài đặt chuẩn (200 dpi, nền trắng, sát mép)."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    import matplotlib.pyplot as plt
    plt.close(fig)
    return path

def setup_matplotlib():
    """Gọi trước khi vẽ matplotlib: phông có dấu tiếng Việt."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "DejaVu Sans"
    return plt

def contact_sheet(img_dir, out_path, cols=4):
    """Ghép tất cả hình thành một tấm ảnh để kiểm tra nhanh bằng mắt."""
    from PIL import Image
    import glob
    ims = [Image.open(f).convert("RGB") for f in sorted(glob.glob(os.path.join(img_dir, "*.png")))]
    for im in ims:
        im.thumbnail((450, 300))
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 460, rows * 310), "white")
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * 460, (i // cols) * 310))
    sheet.save(out_path, quality=80)
    return out_path
