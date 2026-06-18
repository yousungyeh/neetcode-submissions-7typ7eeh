class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        fleet = 1
        l = len(position)
        for i in range(l):
            car.append([position[i], speed[i]])
        sorted_car = sorted(car, key=lambda x: x[0], reverse=True)
        prev_arr_time = 0
        for pos, spd in sorted_car:
            # cur_arr_time = (target-pos+spd-1)//spd
            cur_arr_time = (target-pos)/spd
            print(prev_arr_time, cur_arr_time, pos, spd)
            if not prev_arr_time:
                prev_arr_time = cur_arr_time
            if prev_arr_time < cur_arr_time:
                fleet += 1
                prev_arr_time = cur_arr_time

        return fleet

        