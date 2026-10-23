# 搜狗输入法皮肤

个人收藏与修复的搜狗输入法皮肤（`.ssf`）存档。

皮肤文件由 **Git LFS** 托管，仓库本身很轻；克隆后需要本地装有 Git LFS 才能拿到实体文件（`git lfs install` 一次即可）。

## 皮肤列表

| 皮肤 | 原作 | 状态 | 下载 |
| :-- | :-- | :-- | :-- |
| 逆转裁判 · 成步堂龙一「异议」（动态） | 雪泽歌子 | 已修复 v 模式白底白字 | [成步堂龙一异议-修复版.ssf](skins/gyakuten-naruhodo/成步堂龙一异议-修复版.ssf) |

## 安装

**Windows**

1. 下载 `.ssf` 文件；
2. 双击文件，搜狗会弹出「是否安装该皮肤」，确认即可；
3. 若双击无反应：右键输入法状态栏 → 皮肤 → 皮肤盒子 → 添加本地皮肤，选中 `.ssf`。

**macOS**（搜狗输入法 for Mac 不支持 `.ssf`）

`.ssf` 是 Windows 版皮肤格式，Mac 版使用 `.ssf` 之外的 mac 皮肤包，无法直接导入。

装好后在 属性设置 → 外观 → 皮肤 中切换。候选项排列方式建议选**纵向**，与这套皮肤的竖排底图配套。

## 修复记录

| 皮肤 | 问题 | 处理 |
| :-- | :-- | :-- |
| 成步堂龙一「异议」 | v 模式面板、竖排候选窗白底白字，看不清 | 重绘 `skin2.bmp` / `skin2_1.bmp` / `skin2_2.bmp` 为深蓝底，`separator` 改为 `0x7EA0DF` |

每个皮肤的具体分析见对应目录下的 `NOTES.md`。

## 目录结构

```
skins/
  gyakuten-naruhodo/          逆转裁判 成步堂龙一
    成步堂龙一异议-修复版.ssf
    NOTES.md                  修复分析与已知限制
tools/
  ssf_tool.py                 解包 / 打包 / 查看 .ssf 的小工具
```

`.ssf` 本质是 ZIP 包（内含 `skin.ini` + 若干 BMP/PNG/GIF 切片），用 `tools/ssf_tool.py` 可以直接拆开看：

```bash
python tools/ssf_tool.py list  skins/gyakuten-naruhodo/成步堂龙一异议-修复版.ssf
python tools/ssf_tool.py extract skins/gyakuten-naruhodo/成步堂龙一异议-修复版.ssf ./out
python tools/ssf_tool.py pack  ./out  ./new.ssf
```

## 免责声明

皮肤的美术素材、角色形象版权归原作者（雪泽歌子）及原作权利人（CAPCOM）所有。本仓库仅作个人存档与兼容性修复记录，不用于任何商业用途；如权利人认为不妥，请联系删除。
