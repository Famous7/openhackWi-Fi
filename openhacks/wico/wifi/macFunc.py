from .models import DeviceList

def macHour(mac):
        dic = {}
        output = {}
        dateList = []
        toString = ''
        qs = DeviceList.objects.all().order_by('sniff_time')
        for q in qs:
                if mac in q.mac_list:
                        toString += str(q.sniff_time.year)
                        toString += str(q.sniff_time.month)
                        toString += str(q.sniff_time.day)
                if toString not in dateList:
                        dateList.append(toString)
                        dic[toString] = []
                        output[toString] = 0
                        dic[toString].append(q.sniff_time)
                        toString = ''

        for date in dateList:
                leng = len(dic[date])
                i = 0
                while i < leng-1:
                        v1 = dic[date][i].hour*60 + dic[date][i].minute
                        v2 = dic[date][i+1].hour*60 + dic[date][i+1].minute
                        if v2 - v1 <= 5:
                                output[date] += 5
                        elif i+2 is not leng:
                                v2 = dic[date][i+2].hour*60 + dic[date][i+2].minute
                                if v2 - v1 <= 10:
                                        output[date] += 10
                                i+=1
        return output

def macCalender(mac,s):
        dic = {}
        output = {}
        dateList = []
        toString = ''
        qs = DeviceList.objects.all().order_by('sniff_time')
        for q in qs:
                if mac in q.mac_list:
                        toString += str(q.sniff_time.year)
                        toString += str(q.sniff_time.month)
                        toString += str(q.sniff_time.day)
                if toString not in dateList:
                        dateList.append(toString)
                        dic[toString] = []
                        output[toString] = 0
                        dic[toString].append(q.sniff_time)
                        toString = ''

        for date in dateList:
                leng = len(dic[date])
                i = 0
                while i < leng-1:
                        v1 = dic[date][i].hour*60 + dic[date][i].minute
                        v2 = dic[date][i+1].hour*60 + dic[date][i+1].minute
                        if v2 - v1 <= 5:
                                output[date] += 5
                        elif i+2 is not leng:
                                v2 = dic[date][i+2].hour*60 + dic[date][i+2].minute
                                if v2 - v1 <= 10:
                                        output[date] += 10
                                i+=1
        return output  

