from machine import UART, Pin
import time
from dht import DHT11, InvalidChecksum
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16



sensor = DHT11(Pin(16, Pin.OUT, Pin.PULL_DOWN))
led = Pin(25, Pin.OUT)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
ser = UART(1, 9600)

def main():    
        while True:      
            c=ser.read(1)
            
            while c == b'1':
                
                temp = sensor.temperature
                humidity = sensor.humidity  
                led.value(0)                                        
                lcd.clear()                    
                lcd.move_to(1,0)
                lcd.putstr("Temp: {}°C%".format(temp))
                lcd.move_to(1,1)
                lcd.putstr("Humidity: {:.0f}%".format(humidity))
                            
                time.sleep(2)
                led.value(1)
                       
    
if __name__ == '__main__':
    main()
        

