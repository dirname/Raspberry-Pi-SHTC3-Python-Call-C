# Raspberry Pi SHTC3 Python Call C 
Raspberry Pi Sense HAT (B) SHTC3 温湿度传感器 Python 调用 So 库获取数据示例

这是 __微雪 Sense HAT (B) SHTC3__ 温度传感器 Python 获取数值的一个demo，使用了 C 编译成 so 库再使用 ctypes 调用的例子，解决了在 Python 应用下的局限性

# 环境
+ Raspbian buster
+ GCC 8.3.0 (Raspbian 8.3.0-6+rpi1)

## Sense HAT (B) 传感器
- 板载Raspberry Pi 40pin GPIO接口，适用于Raspberry Pi系列主板
- 板载ICM20948(3轴加速度、3轴陀螺仪和3轴磁力计)，可检测运动姿态、方位和磁场
- 板载SHTC3数字温湿度传感器，可感知环境的温度和湿度
- 板载LPS22HB大气压强传感器，可感知环境的大气压强
- 板载TCS34725颜色识别传感器，可识别周围物体的颜色
- 板载ADS1015芯片，4通道12位精度ADC，可扩展AD功能以便接入更多传感器
- 引出I2C控制接口，方便接入STM32等主控板
- 提供完善的配套资料手册(Raspberry/STM32等示例程序)

[微雪地址官网地址](http://www.waveshare.net/shop/Sense-HAT-B.htm)

如果您想了解更多请阅读 [树莓派4B Sense HAT (B) 使用 Ctypes 来实现 传感器间 C 到 Python 的数值传递](https://blog.forgiveher.cn/2019/11/25/1574671872/)
