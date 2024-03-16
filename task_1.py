class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        if self.head is None:
            print("Список порожній")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Реверс списку
    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self

    # Сортування вставками
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return self
        sorted_list = LinkedList()
        cur = self.head
        while cur:
            next_node = cur.next
            if sorted_list.head is None or sorted_list.head.data >= cur.data:
                cur.next = sorted_list.head
                sorted_list.head = cur
            else:
                prev = sorted_list.head
                while prev.next and prev.next.data < cur.data:
                    prev = prev.next
                cur.next = prev.next
                prev.next = cur

            cur = next_node

        self.head = sorted_list.head
        return self

    # Сортування злиттям
    def merge_sort(self, head=None):
        if head is None:
            head = self.head
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list_head = self.merge(left, right)

        return sorted_list_head

    def get_middle(self, head):
        if head is None:
            return head

        one_step = two_steps = head

        while two_steps.next is not None and two_steps.next.next is not None:
            one_step = one_step.next
            two_steps = two_steps.next.next
        return one_step

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        result = None
        if left.data < right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    def start_merge_sort(self):
        self.head = self.merge_sort()
        return self

    # Об'єднання двох відсортованих списків
    def merge_sorted_lists(self, list1):
        if self.head is None:
            self.head = list1.head
            return self
        if list1.head is None:
            return self

        if self.head.data < list1.head.data:
            current = self.head
            self.head = self.head.next
        else:
            current = list1.head
            list1.head = list1.head.next

        new_head = current
        while self.head and list1.head:
            if self.head.data < list1.head.data:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = list1.head
                list1.head = list1.head.next
            current = current.next

        if self.head:
            current.next = self.head
        elif list1.head:
            current.next = list1.head
        self.head = new_head
        return self


# Тестування
if __name__ == "__main__":
    llist = LinkedList()
    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Заданий зв'язний список:")
    llist.print_list()

    print("\n Реверс списку:")
    llist.reverse_linked_list().print_list()
    print("\n Відсортований список за допомогую сортування вставками:")
    llist.insertion_sort().print_list()

    # Створюємо другий зв'язний список
    llist2 = LinkedList()
    llist2.insert_at_end(45)
    llist2.insert_at_end(15)
    llist2.insert_at_end(30)
    llist2.insert_at_end(60)

    # Сортуємо другий зв'язний список
    print("\n Сортуємо другий зв'язний список за допомогую сортування злиттям:")
    llist2.start_merge_sort().print_list()

    print("\n Об'єднаний зв'язний список:")
    llist.merge_sorted_lists(llist2).print_list()
