import time
import datetime
#
# # 'asctime', 'ctime', 'daylight',
# # 'gmtime', 'localtime', 'mktime',
# #  'sleep', 'strftime', 'time', 'time_ns', 'timezone', 'tzname']
# # print(help(time.asctime))
# print(time.localtime())
# # time.struct_time(tm_year=2023, tm_mon=11, tm_mday=24, tm_hour=21, tm_min=38, tm_sec=55, tm_wday=4, tm_yday=328, tm_isdst=0)
# # t = time.localtime()
# # print(t.tm_year)
#
# # print(time.asctime())
# # print(time.ctime(30000000))
# # time.sleep(10)
# # print(time.daylight)
# # print(time.tzname)
# # print(help(time))
#
# print(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime()))
#

print(datetime.date(2023, 2, 23))
print(datetime.timedelta(-2))
print(datetime.datetime.now())
print(datetime.datetime.now() - datetime.timedelta(-5))

print(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))