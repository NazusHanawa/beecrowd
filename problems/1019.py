raw_seconds = int(input())

hours = raw_seconds // 3600
raw_seconds %= 3600

minutes = raw_seconds // 60
raw_seconds %= 60

seconds = raw_seconds

print(f"{hours}:{minutes}:{seconds}")

