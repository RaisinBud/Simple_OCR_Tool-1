import pytesseract


async def read_image(img_path, lang='eng'):
    """
    Performs OCR on a single image

    :img_path: str, path to the image file
    :lang: str, language to be used while conversion (optional, default is english)

    Returns
    :text: str, converted text from image
    """

    try:
        return pytesseract.image_to_string(img_path, lang=lang)
    except:
        return "[ERROR] Unable to process file: {0}".format(img_path)
    