
class Water:

    def __init__(self, volume = 1, temp = 18):
        self.set_volume(volume)
        self.set_temp(temp)

    def __str__(self):
        return f"WATER <{self.__volume}L | {self.__state} | {self.__temp}C>"

    ################# VOLUME #################
    def set_volume(self, volume): 
        if volume < 1:
            print("ERROR!!! The volume of water is not specified")
        else:
            self.__volume = volume
            
    def get_volume(self):
        return self.__volume
    ################# VOLUME #################

    ################## TEMP ##################
    def set_temp(self, temp): 
        if temp > 2000 or temp < -273:
            print("ERROR!!! No such temperatures for water")
        else:
            self.__temp = temp
            if temp > 100:
                self.__state = "vapor"
            elif temp <= 0:
                self.__state = "solid"
            else:
                self.__state = "liquid"
    def get_temp(self):
        return self.__temp
    ################## TEMP ##################

w = Water()

w.set_temp(20)
w.set_volume(5)

def heat(water, deltaTemp):
    result = Water(water, w.get_temp() + deltaTemp)
    return result

def cool(water, deltaTemp):
    result = Water(water, w.get_temp() - deltaTemp)
    return result
    
print("." * 25)
print(heat(w.get_volume(), 15))       # deltaTemp heat
print("." * 25)
print(heat(w.get_volume(), 95))       # deltaTemp heat
print("." * 25)
print(cool(w.get_volume(), 25))       # deltaTemp cool
print("." * 25)



