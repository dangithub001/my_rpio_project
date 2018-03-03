from RPIO import PWM
import time

DMA_CH = 0
GPin = 21
SSTime = 1000000

PWM.setup(1000,0)
PWM.init_channel(DMA_CH, SSTime)

PWM.add_channel_pulse(DMA_CH, GPin, 0, 20)
PWM.add_channel_pulse(DMA_CH, GPin, 25, 5)
PWM.add_channel_pulse(DMA_CH, GPin, 35, 5)
PWM.add_channel_pulse(DMA_CH, GPin, 45, 5)

time.sleep(5)

PWM.clear_channel_gpio(DMA_CH, GPin)

PWM.cleanup()
