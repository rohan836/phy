C = 299_792_458  # speed of light in m/s

def energy_from_mass(mass_kg: float) -> float:
    return mass_kg * C ** 2

EXAMPLES = [
    ("Paperclip", 0.001),
    ("Human (70 kg)", 70),
    ("Earth", 5.972e24),
    ("Apple", 0.2),
]

def run_examples():
    for name, mass in EXAMPLES:
        e = energy_from_mass(mass)
        print(f"{name:<16} {mass:.3e} kg  ->  {e:.3e} J")
        print()

if __name__ == "__main__":
    run_examples()

    try:
        m = float(input("Enter mass in kg: "))
        e = energy_from_mass(m)
        print(f"E = {m} × ({C})² = {e:.2e} J")
    except ValueError:
        print("Please enter a valid number.")
