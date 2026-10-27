class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  


class StackNodes:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        """Вставляє об'єкт на вершину стеку[cite: 2]"""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Повертає елемент з вершини стеку та видаляє його[cite: 2]"""
        if self.top is None:
            return "Стек порожній"
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        """Повертає елемент з вершини стеку без видалення[cite: 2]"""
        if self.top is None:
            return "Стек порожній"
        return self.top.data

    def clear(self):
        """Видаляє всі елементи зі стеку[cite: 2]"""
        self.top = None
        self._size = 0

    def count(self):
        """Повертає кількість елементів стеку[cite: 2]"""
        return self._size

    def size(self):
        """Повертає кількість елементів у стеку[cite: 2]"""
        return self._size

    def toString(self):
        """Виводить всі елементи стеку, але не видаляє їх[cite: 2]"""
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Стек порожній"



if __name__ == "__main__":
    s = StackNodes()
    
    s.push(11)
    s.push(22)
    s.push(33)
    
    print("Всі елементи стеку (toString):", s.toString())
    print("Вершина стеку (peek):", s.peek())
    print("Кількість елементів (count):", s.count())
    
    print("Витягнуто елемент (pop):", s.pop())
    print("Стек після pop (toString):", s.toString())
    
    s.clear()
    print("Стек після clear (toString):", s.toString())
