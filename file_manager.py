import os
import shutil
sort_need = r""
sort_need = sort_need.replace("\\", "/")
file_list = os.listdir(sort_need)


def checker(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print("Folder %s created!" % path)

def is_folder(folder):
    return os.path.isdir(folder)

def is_screenshot(name):
    if "Screenshot" in name:
        return True
    else:
        return False

def mover(file_location, where):
    shutil.move(file_location, sort_need + where)


documents_list = ["pdf", "docx", "doc", "txt", "rtf", "odt", "pptx", "ppt", "xls", "xlsx", "csv"]
video_list = ["mp4", "mov", "avi", "wmv", "mkv", "flv", "m4v", "webm"]
photo_list = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "raw"]
sound_list = ["mp3", "wav", "flac", "m4a", "aac", "ogg", "wma"]
zip_list = ["zip", "tar", "gz", "bz2", "xz", "7z", "rar"]



for i in file_list:
    file_type = i.split(".")[-1]
    file_location = sort_need + "/" + i
    if is_folder(file_location):
        continue
    if is_screenshot(i):
        checker(sort_need + "/screenshot")
        mover(file_location, "/screenshot")
    elif file_type in photo_list:
        checker(sort_need + "/photo")
        mover(file_location, "/photo")
    elif file_type in video_list:
        checker(sort_need + "/video")
        mover(file_location, "/video")
    elif file_type in documents_list:
        checker(sort_need + "/documents")
        mover(file_location, "/documents")
    elif file_type in zip_list:
        checker(sort_need + "/zip_list")
        mover(file_location, "/zip_list")
    elif file_type in sound_list:
        checker(sort_need + "/sound_list")
        mover(file_location, "/sound_list")
    else:
        checker(sort_need + "/other")
        mover(file_location, "/other")
    
    
print("thats it dawg")


