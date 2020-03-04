#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    # stack
    # bottom [x, x, x, x] top

    # queue
    # top [x, x, x, x] bottom

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)
        print "IN %s" % self.stack_in
        print "OUT %s" % self.stack_out 
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop(-1))
        result = self.stack_out.pop(-1)
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop(-1))

        print "IN %s" % self.stack_in
        print "OUT %s" % self.stack_out 
        return result
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop(-1))
        result = self.stack_out[-1]
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop(-1))
        print "IN %s" % self.stack_in
        print "OUT %s" % self.stack_out 
        return result

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        print "IN %s" % self.stack_in
        print "OUT %s" % self.stack_out 
        if len(self.stack_in) > 0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

