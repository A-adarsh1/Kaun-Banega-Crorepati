import random


__question = [
    ["Q1. Which planet is known as the 'Red Planet'?"],
    ["Q2. Who wrote the famous play 'Romeo and Juliet'"],
    ["Q3. What is the capital of Australia?"],
    ["Q4. In which year did India gain independence from British rule?"],
    ["Q5. What is the chemical symbol for water?"]
]
__options = [
    [
        ["1) Earth"], ["2) Mars"], ["3) Jupiter"], ["4) Venus"]
    ],
    [
        ["1) William Shakespeare"], ["2) Charles Dickens"], ["3) Mark Twain"], ["4) Jane Austen"]
    ],
    [
        ["1) Sydney"], ["2) Melbourne"], ["3) Canberra"], ["4) Brisbane"]
    ],
    [
        ["1) 1942"], ["2) 1945"], ["3) 1947"], ["4) 1950"]
    ],
    [
        ["1) H2O"], ["2) CO2"], ["3) O2"], ["4) NaCl"]
    ]
]
__answers = [
    ["2) Mars"],
    ["1) William Shakespeare"],
    ["3) Canberra"],
    ["3) 1947"],
    ["1) H2O"]
]
__prize_pool = [10000000, 20000000, 20000000, 5000000, 20000000]

balance = 0
lost_money = 0
j = 0
for x, y in zip(__question, __options):
    print(f"Question for Rs. {__prize_pool[j]}")
    print(x[0])
    for i in range(4):
        print(y[i][0])

    given_ans = int(input("Choose the option number : "))
    ans_idx = given_ans - 1
    if __options[j][ans_idx][0] == __answers[j][0]:
        print(f"Your answer is correct.")
        print(f"You won Rs.{__prize_pool[j]} for this question")
        balance += __prize_pool[j]
        print("\n\n")
    else:
        price_money_decreased = random.randint(320000, 640000)
        balance -= price_money_decreased
        lost_money += price_money_decreased
        lost_money += __prize_pool[j]
        print(f"You lose the prize money of Rs. {__prize_pool[j]}")
        print(f"So, rs. {price_money_decreased} is decreased from your winning account")
        print("\n\n")
    j += 1


total = 0
for i in range(5):
    total += __prize_pool[i]
print(f"""
        Gamer Over....

        Total pool prize was rs. {total}
        pool prize you lost rs. {lost_money}

        The total Money you won is Rs. {balance}
""")
