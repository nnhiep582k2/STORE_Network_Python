import ipaddress as ip

if __name__=='__main__':
    class_c = '192.168.0.0'
    source = input('enter prefix (24-30): ')
    network_address = class_c + '/' + source
    print('network address ',network_address)
    network = ip.ip_network(network_address)
    print('total ip: %s'%(network.num_addresses))
    print('network information')
    print('\t netmask: %s'%str(network.netmask))
    print('\t broadcast address: %s'%str(network.broadcast_address))
    start_ip = list(network.hosts())[0]
    end_ip = list(network.hosts())[-1]
    print('\t host from %s to %s'%(start_ip, end_ip))