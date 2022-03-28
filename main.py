class CustomStack():
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop(-1)
    
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def main():
    my_stack = CustomStack()
    sequence = input('Enter you sequence to check whether it is balanced: ')
    for item in sequence:
        if item in ('{', '[', '('):
            my_stack.push(item)
        else:
            if my_stack.isEmpty():
                my_stack.push(item)
                break
            isRight = (
                item == ')' and my_stack.peek() == '(' or
                item == '}' and my_stack.peek() == '{' or
                item == ']' and my_stack.peek() == '['
            )
            if isRight:
                my_stack.pop()
            else:
                break
    print('Your sequence is ', 'not '*(not my_stack.isEmpty()), 'balanced', sep='')
if __name__ == '__main__':
    main()