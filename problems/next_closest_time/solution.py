class Solution:
    def nextClosestTime(self, time: str) -> str:
        hr_d, hr_s, m_d, m_s = int(time[0]), int(time[1]), int(time[3]), int(time[4])
        num_set = sorted({hr_d, hr_s, m_d, m_s})
        i = num_set.index(m_s) + 1
        if i < len(num_set):
            return str(hr_d) + str(hr_s) + ':' + str(m_d) + str(num_set[i])
        i = num_set.index(m_d) + 1
        if i < len(num_set) and num_set[i] < 6:
            return str(hr_d) + str(hr_s) + ':' + str(num_set[i]) + str(num_set[0])
        i = num_set.index(hr_s) + 1
        if i < len(num_set):
            if hr_d < 2:
                return str(hr_d) + str(num_set[i]) + ':' + str(num_set[0]) + str(num_set[0])
            elif num_set[i] < 4:
                return str(hr_d) + str(num_set[i]) + ':' + str(num_set[0]) + str(num_set[0])
        i = num_set.index(hr_d) + 1
        if i < len(num_set) and num_set[i] < 3:
            return str(num_set[i]) + str(num_set[0]) + ':' + str(num_set[0]) + str(num_set[0])
        return str(num_set[0]) + str(num_set[0]) + ':' + str(num_set[0]) + str(num_set[0])