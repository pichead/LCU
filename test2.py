from easymodbus.modbusClient import ModbusClient
import datetime
import time
import mysql.connector
from datetime import datetime
from fun import sixteens_to_int
############################################################################
db = mysql.connector.connect(
    host="27.254.90.149",
    user="weare12we",
    passwd="@Bas290839",
    database="pecdb"
)
print("mySQL connect")
ip = '192.168.16.200'
############################################################################

while True:
    try:
        UnixTime = int(datetime.now().timestamp())
        Datetime = (datetime.utcfromtimestamp(UnixTime).strftime("%y-%m-%d %H:%M:%S"))
        Date = (datetime.utcfromtimestamp(UnixTime).strftime("%y-%m-%d"))
        Time = (datetime.utcfromtimestamp(UnixTime).strftime("%H:%M:%S"))

        modbusclient = ModbusClient(ip, 502)
        modbusclient.connect()
        print("Modbus connect")
        print("*"*15)

        BlockPerString = modbusclient.read_holdingregisters(12290,2)

        String = int(BlockPerString[0])
        Block = int(BlockPerString[1])

        print("Total Block per String :"+str(Block))
        print("Total String :"+str(String))
        print("*"*20)
        #string no.1
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

        # # mycursor = db.cursor()
        # # sql = "INSERT INTO historyvoltage (No_Str, Sum_Volt, B01, B02, B03, B04, Idc, Temp, SOC, WH_sum, WH_cal, WH_rem, UnixTime, Date, Time, RecordingTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # # val = ("1", Vstr1, Vb01, Vb02, Vb03, Vb04, Idc1, Temp1, SOC1, WH_sum, WH_cal, WH_rem, UnixTime, Datetime, Date, Time)
        # # mycursor.execute(sql, val)
        # # db.commit()
        
            print("Vstr : "+str(Vstr)+"V.")
            print("V1dc : "+str(Vb1)+"v.")
            print("V2dc : "+str(Vb2)+"V.")
            print("V3dc : "+str(Vb3)+"V.")
            print("V4dc : "+str(Vb4)+"V.")
            print("Idc : "+str(Idc)+"A.")
            print("Temp : "+str(Temp)+"'C")
            print("SOC : "+str(SOC)+"%")
            print("WH_sum : "+str(WH_sum)+"Vh")
            print("WH_cal : "+str(WH_cal)+"Vh")
            print("WH_rem : "+str(WH_rem)+"Vh")
            print("Insert Complete")
        print("*"*20)
        print("*"*20)
    except Exception as e:
        print(e)

    finally:
        modbusclient.close()
        time.sleep(3)

