import BlynkLib

BLYNK_AUTH = "97c8eb831fb04a989491f8c9760cdfc3"
BLYNK_IP =  "192.168.43.19"
BLYNK_PORT = 9000

blynk = BlynkLib.Blynk(BLYNK_AUTH,BLYNK_IP,BLYNK_PORT)

w = 0
coeff = 0
flag = 0

@blynk.VIRTUAL_WRITE(2)
def v2_read_handler(value):    
    global w
    global coeff
    global flag

    if flag is  0:
        return

    if flag is 1:
        flag = 0

    w = int(value)
    if coeff<0:
        w1 = int(round(w*(1+coeff),0))
        w2 = w
    if coeff>=0:
        w1 = w
        w2 = int(round(w*(1-coeff),0))
    blynk.virtual_write(3,w1)
    blynk.virtual_write(4,w2)


@blynk.VIRTUAL_WRITE(1)
def v1_read_handler(value):
    global coeff
    global flag

    if flag is 1:
        return
    
    if flag is 0:
        flag = 1

    coeff = (int(value)-128)/128
    

blynk.run()
