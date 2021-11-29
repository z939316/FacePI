import fire, json, http.client, urllib.request, urllib.parse, urllib.error, base64

imagepath = "Korea_fish.jpg"
class FacePI:
    def readConfig(self):
        with open("config.json", "r", encoding="utf-8") as f:
            config=json.load(f)
        return config
    def writeConfig(self,config):
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f)
    def setConfig(self):
        config = self.readConfig()
        print("每個參數後[]為預設值，按enter即表示不更動")
        api_key = input(f'請輸入有效的API_KEY：{config["api_key"]}: ')
        if api_key: config["api_key"] = api_key
        title = input(f'請輸入title[{config["title"]}]: ')
        if title: config["title"] = title
        self.writeConfig(config)
    def test(self):
        print(self.readConfig())
        config = self.readConfig()
        print(config["two"])
    def detectImage(self):
        headers = {
            # Request headers
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.readConfig()["api_key"],
        }
        print(self.readConfig()["api_key"])
        requestbody= open(imagepath, "rb").read()
        params = urllib.parse.urlencode({
            # Request parameters
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age, gender',
            'recognitionModel': 'recognition_04',
            'returnRecognitionModel': 'false',
            'detectionModel': 'detection_01',
            'faceIdTimeToLive': '86400',
        })

        try:
            conn = http.client.HTTPSConnection('eastasia.api.cognitive.microsoft.com')
            conn.request("POST", "/face/v1.0/detect?%s" % params, requestbody, headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
if __name__ == '__main__':
    fire.Fire(FacePI)
