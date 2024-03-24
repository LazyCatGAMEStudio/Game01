import imageObj
import const
import random


class Basic(imageObj.Image):
    def __init__(self, fileName, dataFile: dict) -> None:
        super().__init__(
            fileName,
            const.MAIN_PATH,
            dataFile.get("center", (random.randint(30, 370), 0)),
        )
        # self.speed_fwd = dataFile.get("speed_fwd", 0.0)
        self.speed_fwd = 5
        self.speed_down = dataFile.get("speed_down", 0.0)
        self.speed_lt = dataFile.get("speed_lt")
        self.speed_rt = dataFile.get("speed_rt")
        
        assert self.speed_rt and self.speed_lt 

    def __str__(self) -> str:
        return str([type(self.speed_fwd), -self.speed_down, self.speed_lt, self.speed_rt])

    def goFwd(self, mirror=False):
        print("log fwd")
        if not mirror:
            self.rect.move_ip(0, -self.speed_fwd)
        else:    
            self.rect.move_ip(0, self.speed_fwd)

    def goDown(self, mirror=False):
        print("log down")
        if not mirror:
            self.rect.move_ip(0, self.speed_down)
        else:
            self.rect.move_ip(0, -self.speed_down)

    def goLt(self, mirror=False):
        print("log left")
        if not mirror:
            self.rect.move_ip(-self.speed_lt, 0)
        else:
            self.rect.move_ip(self.speed_lt, 0)

    def goRt(self, mirror=False):
        print("log right")
        if not mirror:
            self.rect.move_ip(self.speed_rt, 0)
        else:
            self.rect.move_ip(-self.speed_rt, 0)
