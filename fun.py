from easymodbus.modbusClient import ModbusClient
import mysql.connector
import datetime
import time
from datetime import datetime
ip = '192.168.16.200'

def sixteens_to_int(dc):
    return dc -65536 if dc > 32767 else dc

def Time():
    global UnixTime, Datetime, Date, Time
    UnixTime = int(datetime.now().timestamp())+25200
    Datetime = (datetime.utcfromtimestamp(UnixTime).strftime("%y-%m-%d %H:%M:%S"))
    Date = (datetime.utcfromtimestamp(UnixTime).strftime("%y-%m-%d"))
    Time = (datetime.utcfromtimestamp(UnixTime).strftime("%H:%M:%S"))
    return UnixTime, Datetime, Date, Time

def get_data():
    modbusclient = ModbusClient(ip, 502)
    modbusclient.connect()
    print("Modbus connect")
    print("*"*15)
    BlockPerString = modbusclient.read_holdingregisters(12290,2)
    String = (BlockPerString[0])
    Block = (BlockPerString[1])
    print("Total Block per String :"+str(Block))
    print("Total String :"+str(String))
    print("*"*15)
    for n in range (1, String+1):
        VB = modbusclient.read_holdingregisters(257+(256*(String-1)), Block)
        Vstr = modbusclient.read_holdingregisters(8459+(256*(String-1)), 1)
        Idc = modbusclient.read_holdingregisters(8449+(256*(String-1)), 1)
        SOC = modbusclient.read_holdingregisters(8463+(256*(String-1)), 1)
        Temp = modbusclient.read_holdingregisters(8451+(256*(String-1)), 1)
        WH_sum = modbusclient.read_holdingregisters(8457+(256*(String-1)), 1)
        WH_cal = modbusclient.read_holdingregisters(8460+(256*(String-1)), 1)
        WH_rem = modbusclient.read_holdingregisters(8456+(256*(String-1)), 1)

        print("Str"+str(n)+"recive data")

        Vstr = '%.2f'%(float(Vstr[0]/100))
        Vb1 = '%.3f'%(float(VB[0]/1000))
        Vb2 = '%.3f'%(float(VB[1]/1000))
        Vb3 = '%.3f'%(float(VB[2]/1000))
        Vb4 = '%.3f'%(float(VB[3]/1000))
        dc = float(Idc[0]*1)
        Idc = (sixteens_to_int(dc))/10
        Temp = '%.1f'%(float(Temp[0]/10))
        SOC = (float(SOC[0]/1))
        WH_sum = '%.3f'%(float(WH_sum[0]/10))
        WH_cal = '%.3f'%(float(WH_cal[0]/10))
        WH_rem = '%.3f'%(float(WH_rem[0]/10))
        
        print("Str"+str(n)+"Tranfrom Data")
        print(("time is : ") + Datetime)
        
        return Vstr, Vb1, Vb2, Vb3, Vb4, Idc, Temp, SOC, WH_sum, WH_cal, WH_rem
