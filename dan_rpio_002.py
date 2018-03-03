from RPIO import PWM
import time

DMA_CH = 0
GPin = 21
SSTime = 1000000

PWM.setup(1000,0)
PWM.init_channel(DMA_CH, SSTime)

PWM.add_channel_pulse(DMA_CH, GPin, 0, 200)
PWM.add_channel_pulse(DMA_CH, GPin, 250, 50)
PWM.add_channel_pulse(DMA_CH, GPin, 350, 50)
PWM.add_channel_pulse(DMA_CH, GPin, 450, 50)

time.sleep(5)

PWM.clear_channel_gpio(DMA_CH, GPin)

PWM.cleanup()
