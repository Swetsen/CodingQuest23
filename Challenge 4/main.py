"""Coding Game: Challange 4"""


def decode_packet(packet):
    """Bring singular pack into propper format"""
    header = int(packet[:4], 16)
    if header != 0x5555:
        return None
    ship_num = int(packet[4:12], 16)
    seq_num = int(packet[12:14], 16)
    checksum = int(packet[14:16], 16)
    payload = packet[16:]

    payload_sum = sum(int(payload[i:i+2], 16)
                      for i in range(0, len(payload), 2))
    payload_sum %= 256
    if payload_sum != checksum:
        return None
    return (ship_num, seq_num, payload)


def decode_packets(_packets):
    """Bring multiple packs into propper format"""
    valid_packets = [p for p in _packets if decode_packet(p) is not None]
    valid_packets.sort(key=lambda p: decode_packet(p)[1])

    payload = "".join(decode_packet(p)[2] for p in valid_packets)

    _message = "".join(chr(int(payload[i:i+2], 16))
                       for i in range(0, len(payload), 2))
    return _message.rstrip()


f = open("Challenge 4/data", "r", encoding="utf-8")
f = f.read()
f = f.split("\n")

packets = f
MESSAGE = decode_packets(packets)
print(MESSAGE)
