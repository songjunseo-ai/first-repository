names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for  (name, age) in enumerate(zip(names, ages), start=1):
    print(f"{idx}. {name} - {age}세")
print("hello")
