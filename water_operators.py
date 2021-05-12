class Water:
    def __init__(self, volume = 0):
        if self.isNumber(volume):
            self.volume = volume
        elif type(volume) == str and volume in ["large", "medium", "small"]:
            if volume == "large":
                self.volume = 1000
            elif volume == "medium":
                self.volume = 100
            elif volume == "small":
                self.volume = 10
        else:
            print("ERROR!!! Wrong volume value!!!")
    def __str__(self):
        return f"WATER <{self.volume}L>"
    def __len__(self):
        return self.volume

    def __gt__(self,other):
        if self.isNumber(other):
            return self.volume > other
        else:
            return self.volume > other.volume
    def __add__(self, other):
        return Water(self.volume + other.volume)

    def __lt__(self, other):
        if self.isNumber(other):
            return self.volume < other
    def __ge__(self, other):
        if self.isNumber(other):
            return self.volume >= other
    def __le__(self, other):
        if self.isNumber(other):
            return self.volume <= other
    def __eq__(self, other):
        if self.isNumber(other):
            return self.volume == other
    def __ne__(self, other):
        if self.isNumber(other):
            return self.volume != other
      
    def isNumber(self, value ):
        return type(value) == int or type(value) == float


# emptyWater = Water()
largeWater = Water(1000)
# smallWater = Water(0.5)
weirdWater = Water("medium")

# print(emptyWater)
# print(largeWater)
# print(smallWater)
# print(weirdWater)

####### __gt__ ############
print(largeWater > weirdWater)
###########################

####### __lt__ ############
print(largeWater < 700)
###########################

####### __ge__ ############
print(largeWater >= 500)
###########################

####### __le__ ############
print(largeWater <= 500)
###########################

####### __eq__ ############
print(largeWater == 1000)
###########################

####### __ne__ ############
print(largeWater != 1000)
###########################

# print(largeWater > smallWater)

# resultWater = largeWater + weirdWater
# print(resultWater)