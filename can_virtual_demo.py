import can
import time

print("开始测试虚拟 CAN 通信...")

# 创建两个虚拟 CAN 总线实例，共用同一个 channel
bus_send = can.interface.Bus(interface='virtual', channel='vcan0')
bus_recv = can.interface.Bus(interface='virtual', channel='vcan0')

# 构造一条 CAN 消息：ID 是 0x456，数据是 [0x00, 0x64]（代表车速 100 km/h）
msg = can.Message(
    arbitration_id=0x456,
    data=[0x00, 0x64],
    is_extended_id=False
)

# 发送
bus_send.send(msg)
print(f"✅ 已发送: ID={hex(msg.arbitration_id)}, 数据={msg.data}")

# 等待并接收
time.sleep(0.1)
received = bus_recv.recv(timeout=1.0)

if received:
    print(f"✅ 已接收: ID={hex(received.arbitration_id)}, 数据={received.data}")
    print("🎉 恭喜！你的第一个虚拟 CAN 收发脚本跑通了！")
else:
    print("❌ 未收到消息，请检查代码或报错信息。")
