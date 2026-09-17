# Start

ranks = []

while True:
    try:
        rank = int(input("Enter a rank: "))

        if rank == -999:
            if len(ranks) >= 10:
                break

            print("Need at least 10 valid ranks. keep entering.")
            continue

        if rank < 1 or rank > 5:
            print("Not in range, skip...")
            continue

        ranks.append(rank)

    except ValueError:
        print("Invalid input, skip...")

average_rank = sum(ranks) / len(ranks)
highest_rank = max(ranks)

print()
print(f"Number of valid ranks: {len(ranks)}")
print(f"Average rank: {average_rank:.2f}")
print(f"Highest rank: {highest_rank}")

# Stop