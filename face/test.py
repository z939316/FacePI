import fire, json
class FacePI:
    def readConfig(self):
        with open("config.json", "r", encoding="utf-8") as f:
            config=json.load(f)
        return config
    def test(self):
        print(self.readConfig())
        config = self.readConfig()
        print(config["two"])
if __name__ == '__main__':
    fire.Fire(FacePI)
FacePI.test()