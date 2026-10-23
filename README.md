# 成步堂龙一「异议」搜狗输入法动态皮肤 — V 模式修复版

> 本项目为非官方的搜狗输入法 `.ssf` 皮肤修复版本，并非《逆转裁判》官方作品。
> 仓库用于收藏与修复搜狗输入法皮肤，当前收录 1 款。

原作者：**雪泽歌子** · [B 站主页](https://space.bilibili.com/7233194)

## 下载

| 文件 | 大小 | 校验 | 下载 |
| :-- | :-- | :-- | :-- |
| 成步堂龙一_异议_动态皮肤_V模式修复版.ssf | 121.9 KB | [SHA256SUMS.txt](SHA256SUMS.txt) | **[直接下载](https://media.githubusercontent.com/media/Dithob/sogou-input-skins/main/%E6%88%90%E6%AD%A5%E5%A0%82%E9%BE%99%E4%B8%80_%E5%BC%82%E8%AE%AE_%E5%8A%A8%E6%80%81%E7%9A%AE%E8%82%A4_V%E6%A8%A1%E5%BC%8F%E4%BF%AE%E5%A4%8D%E7%89%88.ssf)** |

皮肤包由 **Git LFS** 托管。上面的直链指向 LFS 媒体服务器，点击即开始下载，**无需登录、无需克隆仓库**。

校验方式：

```bash
# Windows
certutil -hashfile 成步堂龙一_异议_动态皮肤_V模式修复版.ssf SHA256
# macOS / Linux
sha256sum 成步堂龙一_异议_动态皮肤_V模式修复版.ssf
```

结果应与 `SHA256SUMS.txt` 中的 `7659aa607efb25ae285bb2800cff178676a605e6c0e8198b993d842cc97d81a4` 一致。

## 下载与安装

1. 点上方「直接下载」拿到 `.ssf` 文件。
2. Windows 安装搜狗拼音输入法后，双击 `.ssf` 安装皮肤。
3. 切换到该皮肤，输入 `v2` 检查 V 模式候选显示。
4. 若遇到缓存，尝试重新切换皮肤或重启输入法。

## 修复内容

- 将 V 模式相关背景修改为 **RGB(37, 54, 90)** 主色的深蓝渐变，以改善白色候选文字的对比度。
- 删除此前右侧出现的明显竖向装饰线。
- 使用用户提供的金色律师徽章图片，放置在 **右上角**。
- 保留普通输入模式原始文字颜色、原始动态 GIF 及其他普通模式资源。

> 修复版经过压缩包完整性校验，并有安装后截图反馈；不同搜狗版本的实际显示可能略有差异。

问题根因与改动清单见 [notes/成步堂龙一异议-修复分析.md](notes/成步堂龙一异议-修复分析.md)，版本记录见 [CHANGELOG.md](CHANGELOG.md)。

## 已知限制

- `.ssf` 是 Windows 版皮肤格式，**搜狗输入法 for Mac 无法导入**。
- 横排双行方案（`[Scheme_H2]`）沿用原皮肤的浅色底图，若把候选项设为「横向 + 双行」，仍可能出现浅底白字。把候选排列切成**纵向**即可避开。

## 仓库结构

```
成步堂龙一_异议_动态皮肤_V模式修复版.ssf   皮肤本体（Git LFS）
SHA256SUMS.txt                             校验值
CHANGELOG.md                               版本记录
notes/                                     修复分析与技术细节
tools/ssf_tool.py                          ssf 解包 / 打包 / 查看工具
```

`.ssf` 本质是 ZIP 包（`skin.ini` + 若干 BMP/PNG/GIF 切片），可以直接拆开：

```bash
python tools/ssf_tool.py list  成步堂龙一_异议_动态皮肤_V模式修复版.ssf
python tools/ssf_tool.py info  成步堂龙一_异议_动态皮肤_V模式修复版.ssf
python tools/ssf_tool.py extract 成步堂龙一_异议_动态皮肤_V模式修复版.ssf ./out
python tools/ssf_tool.py pack    ./out ./new.ssf
```

## 免责声明

皮肤美术素材、角色形象版权归原作者（[雪泽歌子](https://space.bilibili.com/7233194)）及原作权利人（CAPCOM）所有。本仓库仅作个人存档与兼容性修复记录，不用于任何商业用途；如权利人认为不妥，请联系删除。
