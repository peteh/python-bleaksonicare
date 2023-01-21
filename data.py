from model import Service, Characteristic, ReadWriteNotify
from enums import SonicareState, SonicareBrushType, SonicareValueType, SonicareHandleState, SonicareBrushingMode, SonicareStrength

PREFIX = "477ea600-a260-11e4-ae37-0002a5d5"

# more reverse engineered data: https://blog.johannes-mittendorfer.com/artikel/2020/10/my-toothbrush-streams-gyroscope-data/

RWN = ReadWriteNotify(True, True, True)
R = ReadWriteNotify(True, False, False)
RN = ReadWriteNotify(True, False, True)
RW = ReadWriteNotify(True, True, False)
WN = ReadWriteNotify(False, True, True)
N = ReadWriteNotify(False, False, True)

SERVICES = {
    "0001": Service(
        "Handle", 
        {
            "4010": Characteristic("State", RWN, SonicareValueType.INT8, SonicareHandleState),
            "4020": Characteristic("4020", R, SonicareValueType.INT16),
            "4022": Characteristic("4022", R, SonicareValueType.RAW),
            "4030": Characteristic("4030", RN, SonicareValueType.INT16),
            "4040": Characteristic("4040", RW, SonicareValueType.RAW),
            "4050": Characteristic("Current_Time", RW, SonicareValueType.TIMESTAMP),
        }
    ),
    "0002": Service(
        "Brushing",
        {
            "4070": Characteristic("Current_session_Id", RN, SonicareValueType.INT16),
            "4080": Characteristic("Brushing_Mode", R, SonicareValueType.INT8, SonicareBrushingMode),
            "4082": Characteristic("State", RWN, SonicareValueType.INT8),
            "4090": Characteristic("Active_time", RN, SonicareValueType.INT16),
            "4091": Characteristic("Brushing_Mode2", RN, SonicareValueType.INT8),
            "40a0": Characteristic("40a0", RN, SonicareValueType.INT8),
            "40b0": Characteristic("Strength", SonicareValueType.INT8, SonicareStrength),
            "40c0": Characteristic("40c0", RN, SonicareValueType.INT8),
        }
    ),
    "0004": Service(
        "Session",
        {
            "40d0": Characteristic("Last_Session_Id", RN, SonicareValueType.INT16),
            "40d2": Characteristic("40d2", R, SonicareValueType.INT16),
            "40d5": Characteristic("Session_Type", RW, SonicareValueType.INT8),
            "40e0": Characteristic("Request_Session", WN, SonicareValueType.INT8), # Request session (write session id, write 0x00 to 4110, get notification with data here and at 4100)
            "4100": Characteristic("4100", N, SonicareValueType.INT8), 
            "4110": Characteristic("Session_Access_Control_Point", WN, SonicareValueType.RAW), 
        }
    ),
    "0005": Service(
        "Sensor",
        {
            "4120": Characteristic("Enable", RW, SonicareValueType.INT16), # read not permitted
            "4130": Characteristic("Gyroscope_Data", N, SonicareValueType.RAW), 
            "4140": Characteristic("4140", WN, SonicareValueType.RAW), 
        }
    ),
    "0006": Service(
        "Brush",
        {
            "4210": Characteristic("NFC_Version", R, SonicareValueType.RAW),
            "4220": Characteristic("4220", R, SonicareValueType.INT8),
            "4230": Characteristic("Serial", RN, SonicareValueType.RAW),
            "4240": Characteristic("Date", R, SonicareValueType.STRING),
            "4250": Characteristic("4250", R, SonicareValueType.INT8),
            "4254": Characteristic("4254", R, SonicareValueType.INT8),
            "4260": Characteristic("4260", R, SonicareValueType.INT8),
            "4270": Characteristic("4270", R, SonicareValueType.INT8),
            "4280": Characteristic("Brush_Lifetime_Seconds", R, SonicareValueType.INT16),
            "4290": Characteristic("Brush_Usage_Seconds", R, SonicareValueType.INT16),
            "42a0": Characteristic("Brush_Type", R, SonicareValueType.INT8), # Brush Type (None, Adaptive Clean, Adaptive White, Tongue Care, Adaptive Gums)
            "42a2": Characteristic("42a2", R, SonicareValueType.INT8),
            "42a4": Characteristic("42a4", R, SonicareValueType.RAW),
            "42a6": Characteristic("42a6", RWN, SonicareValueType.INT8),
            "42b0": Characteristic("NFC_Payload", R, SonicareValueType.STRING),
            "42c0": Characteristic("42c0", R, SonicareValueType.INT16),
        }
    ),
    "0007": Service(
        "0007",
        {
            "4310": Characteristic("4310", R, SonicareValueType.INT16),
            "4320": Characteristic("4320", R, SonicareValueType.INT16),
            "4330": Characteristic("4330", R, SonicareValueType.RAW),
            "4360": Characteristic("4360", R, SonicareValueType.RAW), #read not permitted
        }
    ),
    "0008": Service(
        "0008",
        {
            "4410": Characteristic("4410", RW, SonicareValueType.RAW),
            "4420": Characteristic("4420", RW, SonicareValueType.RAW),
        }
    )
}