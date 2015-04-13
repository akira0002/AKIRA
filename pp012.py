import socket 
import sys 
   
NORMAL=0 
ERROR=1 
TIMEOUT=5 
   
def ping(ip,port,timeout=TIMEOUT): 
    try: 
        cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        address=(str(ip),int(port)) 
        status = cs.connect_ex((address)) 
        cs.settimeout(timeout) 
        #this status is returnback from tcpserver 
        if status != NORMAL : 
            print ERROR 
        else: 
            print NORMAL     
    except Exception ,e: 
        print ERROR 
        print "error:%s" %e 
        return ERROR 
       
    return NORMAL 
   
if __name__=='__main__': 
    if len(sys.argv) < 3 : 
        print ur'请按照如下格式使用: ./tcp.py www.sharejs.com 80' 
        sys.exit(1) 
       
    ip = sys.argv[1] 
    port = sys.argv[2] 
    try: 
        timeout = sys.argv[3] 
    except IndexError ,e: 
        timeout=TIMEOUT 
    ping(ip,port,timeout) 
