import requests
import PIL.Image as Image
import numpy as np
def getPictures(upload, code):
    attachments = []
    image = requests.get("http://openweathermap.org/img/wn/" + code + "@2x.png", stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append("photo{}_{}".format(photo["owner_id"], photo["id"]))
    return attachments

def getOnePicture(allCodes):
    if len(allCodes) == 5:
        imageOne = requests.get("http://openweathermap.org/img/wn/" + allCodes[0] + "@2x.png", stream=True)
        with open("file1.png", "wb") as f:
            f.write(imageOne.content)
        imageTwo = requests.get("http://openweathermap.org/img/wn/" + allCodes[1] + "@2x.png", stream=True)
        with open("file2.png", "wb") as f:
            f.write(imageTwo.content)
        imageThree = requests.get("http://openweathermap.org/img/wn/" + allCodes[2] + "@2x.png", stream=True)
        with open("file3.png", "wb") as f:
            f.write(imageThree.content)
        imageFour = requests.get("http://openweathermap.org/img/wn/" + allCodes[3] + "@2x.png", stream=True)
        with open("file4.png", "wb") as f:
            f.write(imageFour.content)
        imageFive = requests.get("http://openweathermap.org/img/wn/" + allCodes[4] + "@2x.png", stream=True)
        with open("file5.png", "wb") as f:
            f.write(imageFive.content)
    elif len(allCodes) == 4:
        imageOne = requests.get("http://openweathermap.org/img/wn/" + allCodes[0] + "@2x.png", stream=True)
        with open("file1.png", "wb") as f:
            f.write(imageOne.content)
        imageTwo = requests.get("http://openweathermap.org/img/wn/" + allCodes[1] + "@2x.png", stream=True)
        with open("file2.png", "wb") as f:
            f.write(imageTwo.content)
        imageThree = requests.get("http://openweathermap.org/img/wn/" + allCodes[2] + "@2x.png", stream=True)
        with open("file3.png", "wb") as f:
            f.write(imageThree.content)
        imageFour = requests.get("http://openweathermap.org/img/wn/" + allCodes[3] + "@2x.png", stream=True)
        with open("file4.png", "wb") as f:
            f.write(imageFour.content)
    elif len(allCodes) == 3:
        imageOne = requests.get("http://openweathermap.org/img/wn/" + allCodes[0] + "@2x.png", stream=True)
        with open("file1.png", "wb") as f:
            f.write(imageOne.content)
        imageTwo = requests.get("http://openweathermap.org/img/wn/" + allCodes[1] + "@2x.png", stream=True)
        with open("file2.png", "wb") as f:
            f.write(imageTwo.content)
        imageThree = requests.get("http://openweathermap.org/img/wn/" + allCodes[2] + "@2x.png", stream=True)
        with open("file3.png", "wb") as f:
            f.write(imageThree.content)
    elif len(allCodes) == 2:
        imageOne = requests.get("http://openweathermap.org/img/wn/" + allCodes[0] + "@2x.png", stream=True)
        with open("file1.png", "wb") as f:
            f.write(imageOne.content)
        imageTwo = requests.get("http://openweathermap.org/img/wn/" + allCodes[1] + "@2x.png", stream=True)
        with open("file2.png", "wb") as f:
            f.write(imageTwo.content)
    elif len(allCodes) == 1:
        imageOne = requests.get("http://openweathermap.org/img/wn/" + allCodes[0] + "@2x.png", stream=True)
        with open("file1.png", "wb") as f:
            f.write(imageOne.content)
    img = Image.new('RGBA', (100 * len(allCodes), 100))
    for i in range(len(allCodes)):
        imgOne = Image.open("file" + str(i + 1) + ".png")
        img.paste(imgOne, (100 * i, 0))
    img.save("image.png")

def getWholePicture(upload):
    attachment = []
    photo = upload.photo_messages("image.png")
    owner_id = photo[0]["owner_id"]
    photo_id = photo[0]["id"]
    access_key = photo[0]["access_key"]
    attachment.append(f"photo{owner_id}_{photo_id}_{access_key}")
    return attachment
