from typing import Optional

class Wizard:

    def __init__(self):
        self.name: Optional[str] = None
        self.level: int = 0

    @staticmethod
    def train(base_level: int) -> "Wizard":
        w = Wizard();
        w.level = base_level
        return w


def main():
    gandalf: Wizard = Wizard.train(7)
    gandalf.level += 1
    print(f"The wizard is now level {gandalf.level}")

if __name__ == '__main__':
    main()