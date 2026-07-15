# matrix_terminal.py
import sys
import time

from tools.startup_founder_dept.investor_pitch_compiler import compile_pitch_narrative
from tools.marketing_agents.ad_copy_gen import generate_ad_copy
from tools.advanced_hardware_dept.power_draw_estimator import estimate_battery_life

def boot_sequence():
    print("⚡ BOOTING CTRL MATRIX...")
    time.sleep(1)
    print("🟢 ALL SYSTEMS NOMINAL. Welcome, Advait.")
    print("========================================")

def main_menu():
    boot_sequence()
    while True:
        print("\n[ MATRIX COMMAND TERMINAL ]")
        print("1. Draft Pitch Narrative")
        print("2. Generate Marketing Copy")
        print("3. Hardware Power Estimator")
        print("0. Shut Down Matrix")
        
        choice = input("\nSelect execution node (0-3): ")
        
        if choice == '1':
            brand = input("Enter brand focus (ctrl/allmate): ")
            print(compile_pitch_narrative(brand_focus=brand))
        elif choice == '2':
            prod = input("Enter product name: ")
            prop = input("Enter core value prop: ")
            print(generate_ad_copy(product_name=prod, value_prop=prop))
        elif choice == '3':
            mah = float(input("Enter Battery mAh: "))
            draw = float(input("Enter System Draw (mA): "))
            print(estimate_battery_life(battery_capacity_mah=mah, total_current_draw_ma=draw))
        elif choice == '0':
            print("Shutting down matrix. Goodbye.")
            sys.exit()
        else:
            print("⚠️ Invalid node selected.")

if __name__ == "__main__":
    main_menu()
