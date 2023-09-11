import time
import Adafruit_ADS1x15

adc=Adafruit_ADS1x15.ADS1115()

G=2/3

adc.start_adc(0,gain=G)

print("ADC Reading Value: ")



while True:

    value=adc.get_last_result()
    p_B=((value-14190)/(4420))*100
    print(round(p_B,0))
    time.sleep(0.5)
