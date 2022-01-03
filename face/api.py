import sys, os, json, time, fire
import http.client, urllib.request, urllib.parse, urllib.error, base64
import ClassApi.ClassFacePI


basepath = os.path.dirname(os.path.realpath(__file__))
configpath = os.path.join(basepath, 'Config.json')
class FacePI:

    def show_opencv(self):
        classes.ClassOpenCV.show_opencv('hint')
    def __init__(self):
        self.detect = ClassApi.ClassFacePI.Face()
    def Signin(self):
        imagepath = "Korea_fish.jpg"
        self.detect.detectLocalImage(imagepath)
        imagepath = classes.ClassOpenCV.show_opencv()
        self.Identify(imagepath)
    def Train(self, userData=None, personname=None):
        """1. 用 3 連拍訓練一個新人"""
        jpgimagepaths = []
        for i in range(3):
            jpgimagepath = classes.ClassOpenCV.show_opencv(
                hint=" (訓練第 " + str(i + 1) + " 張)"
            )
            jpgimagepaths.append(jpgimagepath)

        if personname == None:
            personname = input("請輸入您的姓名: ")

        if userData == None:
            userData = input("請輸入您的說明文字(比如: 高師大附中國一仁): ")

        basepath = os.path.dirname(os.path.realpath(__file__))
        jpgtrainpaths = []
        for jpgimagepath in jpgimagepaths:
            filename = os.path.basename(jpgimagepath)
            # home = os.path.expanduser("~")
            jpgtrainpath = os.path.join(
                basepath, "traindatas", userData, personname, filename
            )
            if not os.path.exists(os.path.dirname(jpgtrainpath)):
                os.makedirs(os.path.dirname(jpgtrainpath))
            os.rename(jpgimagepath, jpgtrainpath)
            jpgtrainpaths.append(jpgtrainpath)

        myconfig = classes.ClassConfig.Config().readConfig()

        personAPI = classes.ClassPerson.Person()
        personAPI.add_personimages(
            myconfig["personGroupId"], personname, userData, jpgtrainpaths
        )
        personGroupapi = classes.ClassPersonGroup.PersonGroup()
        personGroupapi.train_personGroup()
pi = FacePI()
pi.Signin()