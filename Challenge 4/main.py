"""Coding Game: Challange 4"""


def decode_packet(packet):
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


def decode_packets(packets):
    valid_packets = [p for p in packets if decode_packet(p) is not None]
    valid_packets.sort(key=lambda p: decode_packet(p)[1])

    payload = "".join(decode_packet(p)[2] for p in valid_packets)

    message = "".join(chr(int(payload[i:i+2], 16))
                      for i in range(0, len(payload), 2))
    return message.rstrip()


f = open("data", "r")
f = f.read()
f = f.split("\n")

packets = f
message = decode_packets(packets)
print(message)
