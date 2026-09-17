import random
def main():
    answer = random.randint(1,100)
    tries = 0
    print("我想了一个1到100之间的数字，猜猜看。")

    while True:
        guess = input("请输入你的猜测")
        if not guess.isdigit():
            print("请输入整数")
            continue

        guess = int(guess)
        tries += 1

        if guess < answer:
            print("太小了")
        elif guess > answer:
            print("太大了")
        else:
            print(f"猜对了！你用了 {tries} 次。")
            break

if __name__ == "__main__":
    main()

