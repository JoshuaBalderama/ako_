# Silly Python script to output some "poop"
import random
import time

poop_emojis = ['💩', '🧻', '🚽', '😅']

print("Generating poop output...\n")

for i in range(5):
    poop = "poop" + "!" * random.randint(1, 5)
    emoji = random.choice(poop_emojis)
    print(f"{poop} {emoji}")
    time.sleep(0.5)

print("\nFlush complete. 💦🚽")
