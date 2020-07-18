class Solution:
    def reformatDate(self, date: str) -> str:
        dates = date.split()
        months = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04',
                  "May": '05', "Jun": '06', "Jul": '07', "Aug": '08',
                  "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        month = months[dates[1]]
        day = int(dates[0][:-2])
        if day < 10: day = '0' + str(day)
        return '{}-{}-{}'.format(dates[2], month, day)