hours = int(input())
minutes = int(input())

final_hours = hours % 24
final_minutes = minutes + 15

if final_minutes > 59:
    final_hours = (final_hours + 1) % 24
    formatted_minutes = final_minutes % 60
    print(f"{final_hours}:{formatted_minutes:02d}")
else:
    print(f"{final_hours}:{final_minutes}")