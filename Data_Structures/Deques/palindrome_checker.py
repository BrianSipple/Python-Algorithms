from queue import deque


def isPalindrome(string):

    string = str(string)

    d = deque()

    for i in range(len(string)):
        d.append(string[i])

    while len(d) > 0:

        if len(d) == 1:
            return True

        rear = d.pop()
        front = d.popleft()

        if rear != front:
            return False

    return True



if __name__ == '__main__':

    print(isPalindrome('google'))
    print(isPalindrome('goog'))
    print(isPalindrome(1000001))
    print(isPalindrome(1000234))
    print(isPalindrome('madam'))
