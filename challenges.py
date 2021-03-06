class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0:
                dp_table[i][j] = 0
            elif strA[i - 1] == strB[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1]+1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

    return dp_table[rows-1][cols-1]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    if len(items) == 0 or capacity == 0:
        return 0

    weight = items[0][1]
    value = items[0][2]

    if capacity >= weight:
        value_with = value + knapsack(items[1:], capacity - weight)
    else:
        value_with = 0

    value_without = knapsack(items[1:], capacity)
    
    return max(value_with, value_without)

def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for i in range(rows):
        for j in range(cols):
            if i == 0 or j == 0:
                dp_table[i][j] = 0
            elif items[i - 1][1] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                value_with = items[i - 1][2] + dp_table[i - 1][j - items[i - 1][1]]
                value_without = dp_table[i - 1][j]
                dp_table[i][j] = max(value_with, value_without)

    return dp_table[rows - 1][cols - 1]

    return dp_table[rows-1][cols-1]
    
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if len(str1) == 0:
        return len(str2)

    if len(str2) == 0:
        return len(str1)

    str1_last_index = len(str1) - 1
    str2_last_index = len(str2) - 1

    if str1[str1_last_index] == str2[str2_last_index]:
        return edit_distance(str1[:str1_last_index], str2[:str2_last_index])

    return 1 + min(
        edit_distance(str1, str2[:str2_last_index]),
        edit_distance(str1[:str1_last_index], str2),
        edit_distance(str1[:str1_last_index], str2[:str2_last_index])
    )

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for i in range(rows):
        for j in range(cols):
            if i == 0:
                dp_table[i][j] = j
            elif j == 0:
                dp_table[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1]
            else: 
                dp_table[i][j] = 1 + min(
                    dp_table[i][j - 1],
                    dp_table[i - 1][j],
                    dp_table[i - 1][j - 1]
                )

    return dp_table[rows-1][cols-1]
