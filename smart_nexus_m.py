import random
import time

class SmartNexusM:
    def __init__(self):
        # 4 жизненных цикла ровера из вашего README
        self.actions = ["crater_exploration", "plateau_traverse", "hibernation_sleep", "idle_waiting"]
        
        # Хардварные параметры гомеостаза
        self.battery = 100.0
        self.cpu_temp = 50.0
        self.stress_mode = False
        
        # Локальная память (карта местности в % открытых секторов)
        self.mapped_terrain = 50.0 
        
        # Инициализация простой Q-таблицы (состояние -> ценность действий)
        # Состояния: 0 - норма, 1 - стресс (батарея < 35%)
        self.q_table = {
            0: {act: 0.0 for act in self.actions},
            1: {act: 0.0 for act in self.actions}
        }
        self.learning_rate = 0.2
        self.discount_factor = 0.9

    def get_state(self):
        return 1 if self.battery < 35 else 0

    def choose_action(self, state):
        # Стратегия выбора: с вероятностью 10% исследуем новое действие, иначе берем лучшее
        if random.random() < 0.1:
            return random.choice(self.actions)
        return max(self.q_table[state], key=self.q_table[state].get)

    def execute_step(self, step):
        state = self.get_state()
        action = self.choose_action(state)
        
        # Базовый расход энергии из вашего концепта
        power_drain = {"crater_exploration": 6, "plateau_traverse": 4, "idle_waiting": 2, "hibernation_sleep": -5}
        
        # Множитель стресса (активируется при батарее < 35%)
        stress_multiplier = 2.0 if state == 1 else 1.0
        
        # Физика шага
        if action == "hibernation_sleep":
            self.battery = min(100.0, self.battery - power_drain[action]) # Зарядка от солнца
            self.cpu_temp = max(40.0, self.cpu_temp - 2.0)
            reward = 10 if state == 1 else -2 # Спать хорошо только при низком заряде
        else:
            self.battery = max(0.0, self.battery - (power_drain[action] * stress_multiplier))
            self.cpu_temp = min(95.0, self.cpu_temp + (2.0 if action == "crater_exploration" else 0.5))
            
        # Симуляция случайных событий (наезд на камни / аномалии)
        pain_trigger = False
        endorphin_trigger = False
        
        if action == "crater_exploration":
            if random.random() < 0.3: # Риск удара в кратере
                pain_trigger = True
            elif random.random() < 0.4: # Шанс найти науку
                endorphin_trigger = True

        # ЭФФЕКТЫ ГОМЕОСТАЗА
        # 1. Цифровая боль (Memory Degradation)
        if pain_trigger or self.cpu_temp > 85.0:
            lost_data = self.mapped_terrain * 0.01 # Стираем часть кэша памяти
            self.mapped_terrain -= lost_data
            reward = -50
            print(f"💥 [PAIN LOOP]: Механический шок/перегрев! Стерто {lost_data:.2f}% карты.")
            
        # 2. Энергетический стресс (В простое батарея тоже падает!)
        elif action == "idle_waiting":
            reward = -5 # Штраф за лень, время идет
            print("⏳ [TIME PENALTY]: Ровер тратит энергию в простое.")
            
        # 3. Петля эндорфинов (Plasticity Locking)
        elif endorphin_trigger:
            reward = 100
            print("✨ [ENDORPHIN LOOP]: Обнаружена биосигнатура! Память заблокирована в ПЗУ, CPU +20%.")
        else:
            reward = 5 if action == "plateau_traverse" else 0

        # Коррекция Q-таблицы по уравнению Беллмана
        next_state = self.get_state()
        max_next_q = max(self.q_table[next_state].values())
        self.q_table[state][action] += self.learning_rate * (reward + self.discount_factor * max_next_q - self.q_table[state][action])

        print(f"Шаг {step} | Действие: {action} | Батарея: {self.battery:.1f}% | Карта: {self.mapped_terrain:.1f}% | Награда: {reward}")

if __name__ == "__main__":
    rover = SmartNexusM()
    print("🚀 Запуск симуляции цифрового гомеостаза Nexus-M на Марсе...\n")
    for s in range(1, 16):
        rover.execute_step(s)
        time.sleep(0.5)
