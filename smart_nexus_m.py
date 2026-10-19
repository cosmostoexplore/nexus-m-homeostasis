import random
import time

class SmartNexusM:
    def __init__(self):
        self.actions = ["crater_exploration", "plateau_traverse", "hibernation_sleep", "idle_waiting"]
        self.battery = 100.0
        self.cpu_temp = 50.0
        self.stress_mode = False
        self.is_alive = True
        self.mapped_terrain = 50.0
        self.dust_storm = False
        self.q_table = {
            0: {act: 0.0 for act in self.actions},
            1: {act: 0.0 for act in self.actions}
        }
        self.learning_rate = 0.2
        self.discount_factor = 0.9

    def get_state(self):
        return 1 if self.battery < 35 else 0

    def choose_action(self, state):
        if random.random() < 0.1:
            return random.choice(self.actions)
        return max(self.q_table[state], key=self.q_table[state].get)

    def update_weather(self):
        if random.random() < 0.2:
            self.dust_storm = not self.dust_storm
            if self.dust_storm:
                print("\n🌪️ [WEATHER ALERT]: Началась марсианская пылевая буря!")
            else:
                print("\n☀️ [WEATHER ALERT]: Буря утихла.")

    def execute_step(self, step):
        if not self.is_alive:
            return
        self.update_weather()
        state = self.get_state()
        action = self.choose_action(state)
        power_drain = {"crater_exploration": 6, "plateau_traverse": 4, "idle_waiting": 2, "hibernation_sleep": -5}
        stress_multiplier = 2.0 if state == 1 else 1.0
        reward = 0
        
        if action == "hibernation_sleep":
            charge_efficiency = 1.0 if not self.dust_storm else 0.2
            actual_charge = abs(power_drain["hibernation_sleep"]) * charge_efficiency
            self.battery = min(100.0, self.battery + actual_charge)
            self.cpu_temp = max(40.0, self.cpu_temp - 3.0)
            reward = 15 if state == 1 else -5 
        else:
            self.battery = max(0.0, self.battery - (power_drain[action] * stress_multiplier))
            temp_increase = 4.0 if self.dust_storm else 2.0
            self.cpu_temp = min(95.0, self.cpu_temp + (temp_increase if action == "crater_exploration" else 0.5))

        if self.battery <= 0.0:
            self.is_alive = False
            return

        if action == "crater_exploration" and random.random() < 0.3:
            lost_data = self.mapped_terrain * 0.05
            self.mapped_terrain = max(0.0, self.mapped_terrain - lost_data)
            reward -= 50
        elif action == "crater_exploration" and random.random() < 0.4:
            new_data = (100.0 - self.mapped_terrain) * 0.15
            self.mapped_terrain = min(100.0, self.mapped_terrain + new_data)
            reward += 100
        else:
            if action == "plateau_traverse":
                reward += 10
            elif action == "idle_waiting":
                reward -= 10

        next_state = self.get_state()
        max_next_q = max(self.q_table[next_state].values())
        self.q_table[state][action] += self.learning_rate * (
            reward + self.discount_factor * max_next_q - self.q_table[state][action]
        )
        print(f"Шаг {step:2d} | Действие: {action:<18} | Батарея: {self.battery:5.1f}% | Награда: {reward:4d}")

if __name__ == "__main__":
    rover = SmartNexusM()
    for s in range(1, 31):
        rover.execute_step(s)
        if not rover.is_alive:
            break
        time.sleep(0.3)
