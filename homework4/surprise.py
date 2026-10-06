# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

def print_star_names():
    for star in targets:
        print(star)

print_star_names()

def print_star_spectral_type():
    for star in targets:
        print(star, targets[star]["Spectral Type"])
print_star_spectral_type()

def find_stars_with_magnitude_greater_than_0_1():
    for star in targets:
        if targets[star]["Magnitude"] > 0.1:
            print(star, targets[star]["Magnitude"])

find_stars_with_magnitude_greater_than_0_1()

def add_new_target(name, ra, dec, magnitude, spectral_type):
    targets[name] = {
        "RA": ra,
        "Dec": dec,
        "Magnitude": magnitude,
        "Spectral Type": spectral_type
    }

add_new_target("Procyon", "07h 39m 18.1s", "+05° 13′ 30″", 0.34, "F5IV-V")

# def find_brightest_star_near_declination_20():
    #respectfully i looked up how to do this and I need to be honest that i dont understand what I'm doing. 

    