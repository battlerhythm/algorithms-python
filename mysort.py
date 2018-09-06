class BubbleSort():
    def sort(self, l):
        loopCount = len(l)-1
        
        while loopCount != 0:
            for i in range(len(l)-1):
                if l[i] > l[i+1]:
                    l[i], l[i+1] = l[i+1], l[i]
            loopCount -= 1
        
        return l

class InsertionSort():
    def sort(self, l):
        i = 0
        
        while i < len(l)-1:
            j = i
            while j >= 0 and l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                j -= 1
            i += 1
        
        return l

class SelectionSort():
    def sort(self, l):
        ptr = 0
        minVal = None 
        
        while ptr < len(l):
            minVal = l[ptr]
            for i, e in enumerate(l[ptr+1:], ptr+1):
                if e < minVal:
                    minVal = e
                    l[ptr], l[i] = l[i], l[ptr]
            ptr += 1
        
        return l

class MergeSort():
    def sort(self, l):
        if len(l) <= 1:
            return l

        left = l[:len(l)//2]
        right = l[len(l)//2:]
        
        left = self.sort(left)
        right = self.sort(right)
        
        return self.__merge(left, right)

    def __merge(self, left, right):
        result = []
        
        while left and right:
            if left[0] <= right[0]:
                result.append(left[0])
                del left[0]
            else:
                result.append(right[0])
                del right[0]
        
        while left:
            result.append(left[0])
            del left[0]
        
        while right:
            result.append(right[0])
            del right[0]

        return result 
