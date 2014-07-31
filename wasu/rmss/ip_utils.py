
def int_to_binary(v):
    result = bin(int(v))
    result = '%08d' % int(result.split('0b')[-1])
    return result

def ip_to_binary(address):
    li = address.split('.')
    result = [] 
    for value in li:
        result.append(int_to_binary(value))
    return '.'.join(result)

def binary_to_int(binary):
    return '%s' % int(str(binary), 2)

def get_net_mask_binary(subnet_count):
    result = ''
    for i in range(subnet_count):
        result += '1'

    for i in range(32-subnet_count):
        result += '0'
    li = []
    li.append(result[0:8])
    li.append(result[8:16])
    li.append(result[16:24])
    li.append(result[24:32])
    result = '.'.join(li)
    return result

def get_subnet_mask(subnet_count):
    binary = get_net_mask_binary(subnet_count)
    li = binary.split('.')
    result = []
    for item in li:
        result.append(str(int(str(item), 2)))
    return '.'.join(result)

def get_boardcast_address_binary(ip, subnet_mask):
    binary = ip_to_binary(ip)
    li = binary.split('.')
    ip_str = ''
    for item in li:
        ip_str += item

    subnet_count = get_subnet_count(subnet_mask)
    
    boardcast_address_binary = ''
    for i in range(len(ip_str)):
        if i<subnet_count:
            boardcast_address_binary += ip_str[i]
        else:
            boardcast_address_binary += '1'
    binary_list = []
    binary_list.append(boardcast_address_binary[0:8])
    binary_list.append(boardcast_address_binary[8:16])
    binary_list.append(boardcast_address_binary[16:24])
    binary_list.append(boardcast_address_binary[24:32])

    return '.'.join(binary_list)

def get_subnet_count(subnet_mask):
    subnet_mask_binary = ip_to_binary(subnet_mask)
    mask_str = ''
    for item in subnet_mask_binary.split('.'):
        mask_str +=item
    subnet_count = 0
    for v in mask_str:
        if v == '1':
            subnet_count += 1
    return subnet_count

def get_boardcast_address(ip,subnet_mask):
    binary = get_boardcast_address_binary(ip,subnet_mask)
    binary_list = binary.split('.')

    int_list = [] 
    for item in binary_list:
        value = binary_to_int(item)
        int_list.append(value) 
    return '.'.join(int_list)

def get_subnet_address_binary(ip, subnet_mask):
    binary = ip_to_binary(ip)
    li = binary.split('.')
    ip_str = ''
    for item in li:
        ip_str += item
    subnet_count = get_subnet_count(subnet_mask)
    subnet_address_binary = ''
    for i in range(len(ip_str)):
        if i<subnet_count:
            subnet_address_binary += ip_str[i]
        else:
            subnet_address_binary += '0'
    binary_list =[]
    binary_list.append(subnet_address_binary[0:8])
    binary_list.append(subnet_address_binary[8:16])
    binary_list.append(subnet_address_binary[16:24])
    binary_list.append(subnet_address_binary[24:32])
    return '.'.join(binary_list)

def get_subnet_address(ip,subnet_mask):
    binary = get_subnet_address_binary(ip, subnet_mask)
    binary_list = binary.split('.')
    int_list = [] 
    for item in binary_list:
        value = binary_to_int(item)
        int_list.append(value)
    return '.'.join(int_list)

def get_subnet(ip='125.210.229.0', mask_count=24, subnet_block_count=4,host_count=4*256):
    subnet_mask = get_subnet_mask(mask_count)
    max_ip_count = host_count/subnet_block_count
    ip_list = ip.split('.')
    address = ip
    for i in range(subnet_block_count):
       pass  
        
def ip_list_add(seg_list,num):
    res =  int(seg_list[-1])+num
    if res<255:
        del seg_list[-1]
        seg_list.append(res)
        return seg_list
    else:
        res = (int(seg_list[-1])+num) % 256
        del seg_list[-1]
        li = ip_add(seg_list, 1)
        li.append(res)
        return li

def ip_plus(ip,num):
    ip_list = ip.split('.')
    res = ip_list_add(ip_list, num)
    li = []
    for item in res:
        li.append(str(item))
    return '.'.join(li)

#print get_subnet_mask(24)
#print get_boardcast_address('125.210.248.0','255.255.248.0')
#print get_subnet_address('125.210.248.0','255.255.248.0')
print ip_plus('192.168.255.250',10)
