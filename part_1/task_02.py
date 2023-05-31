def int32_to_ip(count):
    part1 = count & 255
    part2 = ((count >> 8) & 255)
    part3 = ((count >> 16) & 255)
    part4 = ((count >> 24) & 255)
    return str(part4) + "." + str(part3) + "." + str(part2) + "." + str(part1)


if __name__ == "__main__":
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"
