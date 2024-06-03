from geopy.distance import geodesic
import sys
import math

MAX_FLOAT = sys.float_info.max

beijing_locations = [
    (39.92, 116.40),      # 故宫，也称为紫禁城
    (39.90, 116.40),      # 天安门广场
    (40.00, 116.28),      # 颐和园
    (40.36, 116.02),      # 八达岭长城
    (39.93, 116.39),      # 北海公园
    (39.92, 116.41),      # 王府井大街
    (39.88, 116.41),      # 天坛公园
    (40.28, 116.249),     # 明十三陵
    (40.35, 116.00),      # 八达岭野生动物世界
    (39.94, 116.40)       # 南锣鼓巷
]

def haversine_distance(coord1, coord2):
    # 将经纬度转换为弧度
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    
    # haversine公式
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    # 地球平均半径，单位为公里
    r = 6371
    return c * r


class NaiveLocationPicker:
    def __init__(self):
        print("Distance Based LocationPicker initialized")

    def recommand_location(self, input_location, favor_num = 3) -> list:
        remaining_locations = beijing_locations[:]
        current_coord = input_location
        chosen_locations = []
        
        for _ in range(favor_num):
            closest_distance = float('inf')
            closest_location = None
            
            for location in remaining_locations:
                # distance = haversine_distance(location, current_coord)
                distance = geodesic(location, current_coord).km
                if distance < closest_distance:
                    # print(distance)
                    closest_distance = distance
                    closest_location = location
            print(closest_distance)
            chosen_locations.append(closest_location)
            remaining_locations.remove(closest_location)
            current_coord = closest_location
        
        return chosen_locations
    

class PopLocationPicker:
    def __init__(self):
        print("Popularity Based LocationPicker initialized")

    def recommand_location(self, input_location, favor_num = 3) -> list:
        tmp_locations = beijing_locations
        rec_locations = []
        cur_loc = input_location
        rec_location = []

        for _ in range(favor_num):
            for loc in tmp_locations:
                distance = geodesic(cur_loc, loc).km
                if distance < MAX_FLOAT:
                    rec_location = loc
            
            rec_locations.append(rec_location)
            idx = tmp_locations.index(rec_location)
            tmp_locations.remove(idx)
            cur_loc = rec_location
        
        return rec_locations
    
class TimeLocationPicker:
    def __init__(self):
        print("Time Based LocationPicker initialized")

    def recommand_location(self, input_location, favor_num = 3) -> list:
        rec_locations = []
        cur_loc = input_location
        rec_location = []

        for _ in range(favor_num):
            for loc in beijing_locations:
                distance = geodesic(cur_loc, loc).km
                if distance < MAX_FLOAT:
                    rec_location = loc
            rec_locations.append(rec_location)
            cur_loc = rec_location
        
        return rec_locations
    
class AILocationPicker:
    def __init__(self):
        print("AI Based LocationPicker initialized")

    def recommand_location(self, input_location, favor_num = 3) -> list:
        rec_locations = []
        cur_loc = input_location
        rec_location = []

        for _ in range(favor_num):
            for loc in beijing_locations:
                distance = geodesic(cur_loc, loc).km
                if distance < MAX_FLOAT:
                    rec_location = loc
            rec_locations.append(rec_location)
            cur_loc = rec_location
        
        return rec_locations