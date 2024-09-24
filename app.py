from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import yt_dlp
import os

app = FastAPI()

# 静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    # 直接提供HTML页面
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


@app.post("/download/")
async def download(
    url: str = Form(...), track_title: str = Form(...), artist_name: str = Form(...)
):
    # 输出文件命名格式为 "曲目名称-艺术家名称.flac"
    output_filename = f"{track_title}-{artist_name}"

    options = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",  # 使用 FFmpeg 提取音频
                "preferredcodec": "flac",  # 指定 FLAC 格式
                "preferredquality": "0",  # 使用最高可能的质量
            }
        ],
        "postprocessor_args": [
            "-metadata",
            f"title={track_title}",
            "-metadata",
            f"artist={artist_name}",
        ],
        "outtmpl": output_filename,
        "quiet": False,
    }

    rel_filename = output_filename + ".flac"
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
        # 由于我们已指定文件名，因此不需要匹配文件模式
        if os.path.exists(rel_filename):
            return FileResponse(
                path=rel_filename, filename=rel_filename, media_type="audio/mpeg"
            )
        else:
            raise HTTPException(status_code=404, detail="File not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
