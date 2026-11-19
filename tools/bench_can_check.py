"""Bench check: open the gs_usb CAN adapter at the pump's bit rate, report it, and always close it."""
import can

bus = can.Bus(interface="gs_usb", channel=0, index=0, bitrate=500000)
try:
    print("opened:", type(bus).__name__, "| channel_info =", repr(bus.channel_info))
    print("state:", bus.state)
finally:
    bus.shutdown()          # runs even if a line above raises
    print("closed OK")
