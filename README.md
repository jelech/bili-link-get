# 🎵 Bilibili 音频下载器

一个简单的 Bilibili 音频下载器，允许用户直接输入URL从 Bilibili 下载音频并转换为 FLAC 格式。

## 🚀 使用方法

1. **拉取并运行 Docker 镜像**：

```bash
   docker run -p 8000:8000 --rm -v $(pwd):/app bili-link-get
```

   如果需要在后台运行，请添加 -d 参数：

```bash
   docker run -p 8000:8000 -d --rm -v $(pwd):/app bili-link-get
```

1. **访问应用**：在浏览器中打开 `http://localhost:8000`，输入你想下载的 Bilibili 视频链接、曲目名称和艺术家名称，然后点击“Download”按钮。

## 🍪 获取 Cookie（用于高级音频）

如果需要下载需要登录的高级音频，你需要从浏览器获取你的 Bilibili Cookie。以下是具体步骤：

1. **安装浏览器插件**：
   - 推荐使用 [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/).

2. **导出 Cookie**：
   - 打开 Bilibili 网站并登录你的账户。
   - 点击浏览器右上角的 EditThisCookie 图标。
   - 选择“导出”按钮，将 Cookie 导出为文本格式。

3. **保存 Cookie**：
   - 将导出的内容保存到文件 `www.bilibili.com_cookies.txt`。


## 🤝 贡献

欢迎提交 Issues 和 Pull Requests，感谢你的参与！

## 📜 License

此项目使用 MIT 许可证，详细信息请查看 [LICENSE](LICENSE) 文件。
