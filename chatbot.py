import requests
import json
from faq_data import DESTINATIONS

url = "https://api.scaledown.xyz/compress/raw/"
current_destination = None

print("Travel Bot: Hello! Ask me about travel destinations.\n")

while True:
    user_input = input("Traveler: ")
    text = user_input.lower()

    # DAYS TO STAY
    if ("day" in text or "stay" in text):
        for dest in DESTINATIONS:
            if dest in text or current_destination == dest:
                current_destination = dest
                print(f"\nTravel Bot: {DESTINATIONS[dest]['days']}")
                break

    # VISA
    elif "visa" in text:
        for dest in DESTINATIONS:
            if dest in text or current_destination == dest:
                current_destination = dest
                print(f"\nTravel Bot: Visa information for {dest.title()}:")
                print(DESTINATIONS[dest]["visa"])
                break

    # BEACHES
    elif "beach" in text and current_destination:
        beaches = DESTINATIONS[current_destination]["beaches"]
        if beaches:
            print(f"\nTravel Bot: Top beaches in {current_destination.title()}:")
            for b in beaches:
                print("-", b)
        else:
            print("\nTravel Bot: This destination is not famous for beaches.")

    # DESTINATION SPOTS
    elif any(dest in text for dest in DESTINATIONS):
        for dest in DESTINATIONS:
            if dest in text:
                current_destination = dest
                print(f"\nTravel Bot: Popular spots in {dest.title()}:")
                for spot in DESTINATIONS[dest]["spots"]:
                    print("-", spot)
                break

    # GENERAL PLACES
    elif "place" in text or "destination" in text:
        print("\nTravel Bot: Popular destinations:")
        for d in DESTINATIONS:
            print("-", d.title())

    elif text in ["exit", "quit"]:
        break

    else:
        print("\nTravel Bot: Sorry, I don't have that information.")
