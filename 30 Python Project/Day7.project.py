                        #  Live Time Display
                        # TickTock Terminal

import time 
import os 
 
# ANSI color codes
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'




def draw_clock():
    try:
        while True:
            
            os.system('cls' if os.name == 'nt' else "clear")
            current_time = time.strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
            current_date = time.strftime('%A, %d %B %Y')  # Full readable date

            # Draw the clock with color
            
            print(GREEN + "       *** ***" + RESET)
            print(GREEN + "      *       *" + RESET)
            print(GREEN + "    *           *" + RESET)
            print(GREEN + f"  *  {CYAN}{current_time.center(11)}{GREEN}  *" + RESET)
            print(GREEN + "   *             *" + RESET)
            print(GREEN + "    *           *" + RESET)
            print(GREEN + "     *         *" + RESET)
            print(GREEN + "       *** ***\n" + RESET)

            # Print date and instruction
            print(YELLOW + f"📅 {current_date}" + RESET)
           
            print("⏰ Press Ctrl+C to stop the clock.")
            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n🛑 Clock Stopped At: {time.strftime('%I:%M:%S %p')}")
        print("👋  Thank you, Ayush!")

if __name__ == "__main__":
    draw_clock()
