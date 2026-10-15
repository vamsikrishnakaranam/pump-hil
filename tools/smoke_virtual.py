"""Smoke test: send one CAN frame on python-can's in-process virtual bus and receive it."""
import can

tx = can.Bus(interface="virtual", channel="pump")
rx = can.Bus(interface="virtual", channel="pump")
tx.send(can.Message(arbitration_id=0x100, data=[1, 2, 3], is_extended_id=False))
print(rx.recv(timeout=1.0))
tx.shutdown()
rx.shutdown()
