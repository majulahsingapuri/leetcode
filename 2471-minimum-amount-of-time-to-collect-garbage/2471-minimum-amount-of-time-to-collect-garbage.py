class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        garbage_mins = 0
        last_m_house = 0
        last_p_house = 0
        last_g_house = 0
        
        for i, house in enumerate(garbage):
            garbage_mins += len(house)
            
            if "M" in house:
                last_m_house = i
            if "P" in house:
                last_p_house = i
            if "G" in house:
                last_g_house = i
                
        travel_mins = 0
        for house in [last_m_house, last_p_house, last_g_house]:
            for time in travel[:house]:
                travel_mins += time
        
        return garbage_mins + travel_mins
            