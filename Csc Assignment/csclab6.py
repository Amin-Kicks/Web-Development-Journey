import statistics
class Sequence:
    def __init__(self, numbers):
        self.numbers= numbers
    def mean(self):
        return statistics.mean(self.numbers)
    def median(self):
        return statistics.median(self.numbers)
    def mode(self):
        try:
            return statistics.mode(self.numbers)
        except statistics.StatisticsError:
            return "No unique mode found"

numbers = []

for i in range(9):
    num = int(input("Enter a number: "))
    numbers.append(num)

seq = Sequence(numbers)

print(f'The median of numbers is {seq.median()}')
print(f'The mean of the numbers is {seq.mean()}')
print(f' The mode of the numbers is {seq.mode()}')