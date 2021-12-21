class Fib():
    def __init__(self):
        self.memo = {0:0, 1:1}

    def fibonacci(self, num):
        if num in self.memo.keys():
            return self.memo[num]
        else: ## 클래스 메서드안에서 메서드 호출시 self 필요
            result = self.fibonacci(num-1) + self.fibonacci(num-2)            
            self.memo[num] = result
            return result
            
def main():
    fib = Fib() #fib인스턴스 만듦
    print(fib.fibonacci(10)) # should return 55

if __name__ == "__main__":
    main()