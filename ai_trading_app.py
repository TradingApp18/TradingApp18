import time
import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def alert():
    print("🔔 Signal found! Take action!")

def main():
    print("📈 AI Trading Signal App Started")
    config = load_config()

    while True:
        print("🔄 Refreshing data...")
        signal = True  # Placeholder logic
        if signal and config.get("sound_alert", True):
            alert()
        time.sleep(config.get("refresh_minutes", 15) * 60)

if __name__ == "__main__":
    main()
