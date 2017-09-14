class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.queue.isempty():
            self.queue.push(x)
            return
        _tmp = Stack()
        while (self.queue.size()):
            _tmp.push(self.queue.pop())
        self.queue.push(x)
        while (_tmp.size()):
            self.queue.push(_tmp.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if self.queue.size() else True


class Stack(object):
    def __init__(self):
        self.mstack = []

    def push(self, x):
        self.mstack.append(x)

    def pop(self):
        return self.mstack.pop()

    def size(self):
        return len(self.mstack)

    def isempty(self):
        return False if len(self.mstack) else True

    def peek(self):
        return self.mstack[-1]


        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()