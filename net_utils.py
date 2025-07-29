def ip_to_i(mask: str) -> int:
    a = int("".join([f"{x:08b}" for x in map(int, mask.split('.'))]), 2)
    return a
    
def slash_mask(mask: str) -> int:
    a = int(mask.lstrip("/"))
    a = '1'*a+'0'*(32-a)
    return int(a, 2)    

def maski(mask: str) -> int:
    if mask.count('.') == 3:
        return ip_to_i(mask)
    else:
        return slash_mask(mask)
        
def mask_to_str(mask: int) -> str:
    a = f"{mask:032b}"
    return '.'.join(str(int(a[i:i+8], 2)) for i in range(0, 32, 8))

def mask_to_slash(mask: int) -> str:
    a = f"{mask:032b}"
    return '/' + str(a.count('1'))

def pr(ip: str, mask: str):
    ip_i = ip_to_i(ip)
    mask_i = maski(mask)
    start = ip_i & mask_i
    end = start | (~mask_i & 0xFFFFFFFF)
    print(f"Range: {mask_to_str(start)} - {mask_to_str(end)}")
    
def ip4():
    private_ranges = [
        ("10.0.0.0", "/8"),
        ("172.16.0.0", "/12"),
        ("192.168.0.0", "/16")
    ]
    for start_ip, mask in private_ranges:
        print(f"{start_ip}{mask}:")
        pr(start_ip, mask)
        
def mask_eq(mask:str):
    if mask.count('.') == 3:
        print(mask_to_slash(maski(mask)))
    else:
        print(mask_to_str(maski(mask)))

import sys

if len(sys.argv) == 3:
    ip = sys.argv[1]
    mask = sys.argv[2]
    pr(ip, mask)
else:
    print("Usage:")
    print("Provide an IP address and a subnet mask as arguments.")
    print("Example: ./ip_range 192.168.1.1 /24")
    print("or ./ip_range 192.168.1.1 255.255.255.0")