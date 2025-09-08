names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for  (name, age) in enumerate(zip(names, ages), start=1):
    print(f"{idx}. {name} - {age}세")
print("새우먹고싶다")
print("짬뽕먹고싶다")
print("짜장면먹고싶다")

