def decode_packet(packet):
    header = int(packet[:4], 16)
    if header != 0x5555:
        return None  # invalid packet, discard it
    ship_num = int(packet[4:12], 16)
    seq_num = int(packet[12:14], 16)
    checksum = int(packet[14:16], 16)
    payload = packet[16:]
    # calculate checksum
    payload_sum = sum(int(payload[i:i+2], 16)
                      for i in range(0, len(payload), 2))
    payload_sum %= 256
    if payload_sum != checksum:
        return None  # invalid checksum, discard packet
    return (ship_num, seq_num, payload)


def decode_packets(packets):
    # filter out invalid packets and sort by sequence number
    valid_packets = [p for p in packets if decode_packet(p) is not None]
    valid_packets.sort(key=lambda p: decode_packet(p)[1])
    # concatenate payloads in correct order
    payload = "".join(decode_packet(p)[2] for p in valid_packets)
    # convert payload to human-readable message
    message = "".join(chr(int(payload[i:i+2], 16))
                      for i in range(0, len(payload), 2))
    return message.rstrip()  # discard trailing spaces


f = open("data", "r")
f = f.read()
f = f.split("\n")
# example usage
packets = f
message = decode_packets(packets)
print(message)  # output: "This is a test. This is a test. Thankyou."
