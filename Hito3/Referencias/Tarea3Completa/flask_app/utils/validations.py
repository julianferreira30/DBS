import filetype


def validate_img(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if conf_img is None:
        return False

    # check if the browser submitted an empty file
    if conf_img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(conf_img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validate_name(name):
    if name is None:
        return False
    
    return len(name) >= 4 and len(name) <= 80

def validate_email(email):
    if email is None:
        return False
    return "@" in email

def validate_phone_number(phone):
    if phone is None:
        return False
    return len(phone) == 9

def validate_text(text):
    if text is None:
        return False
    return len(text) >= 5 and len(text) <= 200

def validate_years(years):
    if years is None:
        return False
    return years >= 1 and years <= 99

def validate_donation(name, email, phone, years):
    return validate_name(name) and validate_email(email) \
        and validate_phone_number(phone) and validate_years(years)

def validate_contact(name, email, phone):
    return validate_name(name) and validate_email(email) \
        and validate_phone_number(phone) 

def validate_comment(name, text):
    return validate_name(name) and validate_text(text)