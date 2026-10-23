#!/usr/bin/env python3
"""搜狗输入法皮肤 .ssf 解包 / 打包 / 查看小工具（仅依赖标准库）。

.ssf 本质是 ZIP 包：skin.ini + 若干 BMP/PNG/GIF 切片。
skin.ini 为 UTF-16 LE + BOM，改写时务必保持原编码，否则皮肤名读不出来。

用法:
    python ssf_tool.py list    <skin.ssf>
    python ssf_tool.py info    <skin.ssf>
    python ssf_tool.py extract <skin.ssf> <目录>
    python ssf_tool.py pack    <目录> <新皮肤.ssf>
"""

import os
import sys
import zipfile


def cmd_list(path):
    with zipfile.ZipFile(path) as z:
        for i in z.infolist():
            print(f"{i.file_size:>9}  {i.filename}")
        print(f"\n共 {len(z.infolist())} 个文件")


def cmd_info(path):
    with zipfile.ZipFile(path) as z:
        if "skin.ini" not in z.namelist():
            print("不是有效的 ssf：包内没有 skin.ini")
            return
        raw = z.read("skin.ini")
        enc = "utf-16" if raw[:2] in (b"\xff\xfe", b"\xfe\xff") else "utf-8"
        text = raw.decode(enc, errors="replace")
        for line in text.splitlines():
            s = line.strip()
            if s.startswith("[") or "=" in s:
                print(line)
        print(f"\n(编码 {enc}, 共 {len(text.splitlines())} 行)")


def cmd_extract(path, outdir):
    os.makedirs(outdir, exist_ok=True)
    with zipfile.ZipFile(path) as z:
        for i in z.infolist():
            target = os.path.join(outdir, i.filename)
            os.makedirs(os.path.dirname(target) or outdir, exist_ok=True)
            with z.open(i) as src, open(target, "wb") as dst:
                dst.write(src.read())
            print("extracted", i.filename)
    print(f"\n-> {outdir}")


def cmd_pack(srcdir, outpath):
    if not os.path.isfile(os.path.join(srcdir, "skin.ini")):
        print("错误：目录下找不到 skin.ini")
        return 1
    names = sorted(
        n for n in os.listdir(srcdir) if os.path.isfile(os.path.join(srcdir, n))
    )
    with zipfile.ZipFile(outpath, "w", zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.write(os.path.join(srcdir, n), n)
            print("packed", n)
    print(f"\n-> {outpath} ({os.path.getsize(outpath)} bytes)")
    return 0


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    cmd = sys.argv[1]
    if cmd == "list":
        cmd_list(sys.argv[2])
    elif cmd == "info":
        cmd_info(sys.argv[2])
    elif cmd == "extract":
        cmd_extract(sys.argv[2], sys.argv[3])
    elif cmd == "pack":
        return cmd_pack(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
