'''
Input: an integer
Returns: an integer
'''
total = 1
def eating_cookies(n, total = 1):
    # Your code here    
    for i in range(n):
        total += 4    

        


    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
