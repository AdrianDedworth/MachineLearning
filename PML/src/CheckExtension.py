ALLOWED_EXTENSIONS = set(['mp4', "avi", "wmv", "mpg", "png"])

def allowed_file(file):
    file = file.split('.')
    if file[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False
