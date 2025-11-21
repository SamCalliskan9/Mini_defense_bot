
... import random
... import time
... 
... def scan_environment():
...     """Sensör simülasyonu: 0 = temiz, 1 = engel, 2 = düşman"""
...     return random.choice([0, 0, 1, 2])
... 
... def choose_action(data):
...     """Karar verme algoritması"""
... 
...     if data == 0:
...         return "MOVE_FORWARD"
...     elif data == 1:
...         return "AVOİD OBTACLE"
...     elif data == 2:
...         return "ENGAGE_TARGET"
... 
... def engage_target():
...     """Saldırı algoritması"""
...     hit_chance = random.randint(1,100)
... 
...     if hit_chance > 60:
...         return "TARGET_NEUTRALİZEDE"
...     else:
...         return "TARGET_ESCAPED"
... 
... def defense_bot_loop():
...     print("=== MINI DEFENSE BOT SYSTEM ===")
...     print("System online. Beginning patrol...\n")
... 
...     while True:
...         sensor = scan_environment()
...         action = choose_action(sensor)
... 
        print(f"[SENSOR DATA] {sensor}")
        print(f"[ACTION] {action}")

        if action == "ENGAGE_TARGET":
            result = engage_target()
            print(f"[COMBAT RESULT] {result}")

        time.sleep(1)

        cmd = input("Continue patrol? (y/n): ").lower()
        if cmd != "y":
            print("Shutting down system...")
            break

if __name__ == "__main__":
    defense_bot_loop()






