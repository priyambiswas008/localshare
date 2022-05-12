###     LocalShare is a command line app using python flask and tailwind css
###     Developed by Priyam Riddha Biswas. Email: priyambiswas71.pb@gmail.com

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os, pathlib

# Getting Script path and changing current directory to script directory
# "files" directory is necessary to store files. it must be in the same directory with the script or executable
script_path = pathlib.Path(__file__)
script_dir = script_path.cwd()
UPLOAD_FOLDER = pathlib.Path("files").absolute()
try:
    os.mkdir(UPLOAD_FOLDER)
    print(f"\n\nCreating 'Files' folder(directory) at {UPLOAD_FOLDER}\n\n")
except:
    print(f"\n\nFiles dir exists at {UPLOAD_FOLDER}\n\n")
    pass
os.chdir(script_dir)


app = Flask(__name__)


# Function to detect file type
def get_file_icon(file):
    image_types = [".ai",".bmp",".gif",".ico",".jpeg",".jpg",".png",".psd",".svg",".tiff",".tif"]
    video_types = [".3gp",".avi",".flv",".m4v",".mkv",".mov",".mp4",".wmv"]
    audio_types = [".aif",".cda",".mp3",".mpa",".ogg",".wav",".wma"]
    disc_types = [".dmg",".bin","iso",".vcd"]
    binary_types = [".apk",".bat",".bin",".com",".exe",".jar",".msi",".py"]
    document_types = [".doc",".docx",".odt",".pdf",".rtf",".txt",".tex",".wpd"]
    compressed_types = [".7z",".arj",".deb",".pkg",".rar",".rpm",".tar.gz",".z",".zip"]

    file_extension = pathlib.Path(file).suffix
    
    if file_extension in image_types:
        return "image.png"
    elif file_extension in video_types:
        return "video.png"
    elif file_extension in audio_types:
        return "audio.png"
    elif file_extension in disc_types:
        return "cloud.png"
    elif file_extension in binary_types:
        return "exe.png"
    elif file_extension in document_types:
        return "document.png"
    elif file_extension in compressed_types:
        return "7zip.png"
    else:
        return "code.png"

# Function to generate html snippet for each file available in "files" directory
def get_files_html():
    raw_html_list = []
    files_list = os.listdir("files/")
    files_list.sort(reverse=True)
    for file_name in files_list:
        file_icon = get_file_icon(file_name)
        file_html = f"""<a href="{ url_for('download', filename=file_name) }" target="_blank">
                        <div class="flex flex-row items-start justify-center w-full m-1">
                            <img src="/static/icons/{file_icon}" class="h-7">
                            <span class="downloadSpan text-xl overflow-y-hidden overflow-x-visible h-8 w-full rounded-lg cursor-pointer pl-2 mb-1 pr-2" style="background: #4b5563;">
                                {file_name}
                            </span>
                        </div>
                    </a>"""
        raw_html_list.append(file_html)
        
    raw_html = "\n".join(raw_html_list)
    return raw_html


@app.route('/')
def index():
    available_files = get_files_html()
    return render_template('app.html',available_files=available_files)

@app.route('/', methods=['POST'])
def upload_file():
    selected_files = request.files.getlist('file')
    for file in selected_files:
        selected_filename = file.filename
        file.save(pathlib.Path(f"{UPLOAD_FOLDER}/{selected_filename}"))

    return redirect(url_for('index'))

@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=False, threaded=True)