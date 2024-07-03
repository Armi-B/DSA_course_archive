class Teacher:
    def __init__(self, presentation, proper_day, anger):
        self.anger = anger
        self.presentation = presentation
        self.proper_day = proper_day
    
class MinHeap:
    def __init__(self):
        self.heap = []

    def bubble_up(self, index):
        while index != 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index].anger > self.heap[index].anger:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def bubble_down(self, index):
        while (2 * index + 1) < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_index = left_child_index
            if (right_child_index < len(self.heap) 
                and self.heap[right_child_index].anger < self.heap[left_child_index].anger):
                min_index = right_child_index
            if self.heap[index].anger > self.heap[min_index].anger:
                self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
                index = min_index
            else:
                break

    def heap_push(self, new_node):
        self.heap.append(new_node)
        self.bubble_up(len(self.heap) - 1)

    def heap_pop(self):
        min_val = self.heap[0].anger
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 0:
            self.bubble_down(0)
        return min_val

    def is_empty(self):
        return len(self.heap) == 0
    
    def return_root(self):
        return self.heap[0]

inp = input().split()
days_num = int(inp[1])
teachers_num = int(inp[0])

teachers = []
tot_anger = 0

for _ in range(teachers_num):
    day, presentation, anger = map(int, input().split())
    teacher = Teacher(presentation, day, -anger)
    tot_anger += presentation * anger
    teachers.append(teacher)

teachers_max_heap = MinHeap()
day_teacher_map = {day: [] for day in range(1, days_num+1)}

for teacher in teachers:
    day_teacher_map[teacher.proper_day].append(teacher)

for day in range(1, days_num + 1):
    for teacher in day_teacher_map[day]:
        teachers_max_heap.heap_push(teacher)

    while not teachers_max_heap.is_empty() and teachers_max_heap.return_root().presentation == 0:
        teachers_max_heap.heap_pop()

    if not teachers_max_heap.is_empty():
        tot_anger += teachers_max_heap.return_root().anger
        teachers_max_heap.return_root().presentation -= 1

print(tot_anger)