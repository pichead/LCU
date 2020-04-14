from easymodbus.modbusClient import ModbusClient
import mysql.connector
import datetime
import time
from datetime import datetime


def sixteens_to_int(dc):
    return dc -65536 if dc > 32767 else dc

def TimeNow():
    UnixTime = int(datetime.now().timestamp())
    Datetime = (datetime.utcfromtimestamp(UnixTime).strftime("%y-%m-%d %H:%M:%S"))
    Date = (datetime.utcfromtimestamp(UnixTime).strftime("%y-%m-%d"))
    Time = (datetime.utcfromtimestamp(UnixTime).strftime("%H:%M:%S"))
    return UnixTime, Datetime, Date, Time

def modbusConnecter(ip):
    modbusclient = ModbusClient(ip, 502)
    modbusclient.connect()
    print("Modbus connect")
    print("*"*15)
    return modbusclient

def String_Block_reader(modbusclient):
    BlockPerString = modbusclient.read_holdingregisters(12290,2)
    String = int(BlockPerString[0])
    Block = int(BlockPerString[1])
    print("Total Block per String :"+str(Block))
    print("Total String :"+str(String))
    print("*"*20)
    return String, Block