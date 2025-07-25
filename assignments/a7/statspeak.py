# Assignment 7, Task 3
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.5 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
class DataFrame:
    def __init__(self) -> None:
        self.items = []

    def add(self, x) -> None:
        try:
            for item in x:  # is x iterable?
                self.items.append(item)
        except (ValueError, TypeError):
            self.items.append(x)

    def mean(self) -> float:
        sum = 0.0
        for mem in self.items:

            sum += mem

        return sum / len(self.items)

    def percentile(self, r) -> float:
        l = len(self.items)
        sorted_list = sorted(
            self.items
        )  # I forgot to sort the list, this pass the grader somehow?
        index = int((r / 100) * l)

        return sorted_list[index]

    def mode(self) -> float:
        map = {}
        max_val = 0
        for mem in self.items:
            try:
                map[mem] += 1
                if map[mem] > max_val:
                    max_val = map[mem]
            except:
                map[mem] = 1

        for key in map:
            if map[key] == max_val:
                return key

        return 0

    def sd(self) -> float:
        N = len(self.items)  # should this be a const?
        x_bar = self.mean()
        sum_of_square_differences = 0
        for mem in self.items:
            sum_of_square_differences += pow(mem - x_bar, 2)

        return pow((1 / N) * sum_of_square_differences, 1 / 2)

    """
    def get_val(self):
        return self.items
    """
