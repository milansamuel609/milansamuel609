import datetime
import random

def generate_random_date():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date.today()
    random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

def generate_snake():
    snake_length = 25  # Change this to adjust the snake's length
    contributions = []

    for _ in range(snake_length):
        date = generate_random_date()
        contributions.append(date)

    return contributions

if __name__ == "__main__":
    snake = generate_snake()
    for date in snake:
        print(date)
