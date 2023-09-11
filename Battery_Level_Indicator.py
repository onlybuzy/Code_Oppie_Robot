import time
import Adafruit_ADS1x15

adc=Adafruit_ADS1x15.ADS1115()

G=2/3

adc.start_adc(0,gain=G)

print("ADC Reading Value: ")



while True:

    value=adc.get_last_result()
    b_B=map(value,)*100/4095
    print('Channel 0: {0.00}'.format(b_B))
    time.sleep(0.5)
