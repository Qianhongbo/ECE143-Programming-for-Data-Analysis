def get_trapped_water(seq):
    """

    :param seq: an input list
    :return: how many units of water remain trapped between the walls in the map
    """
    assert isinstance(seq, list)

    if not seq:
        return 0

    left, right = 0, len(seq) - 1
    left_max, right_max = seq[left], seq[right]
    water = 0
    while left <= right:
        if left_max < right_max:
            left_max = max(left_max, seq[left])
            water += left_max - seq[left]
            left += 1
        else:
            right_max = max(right_max, seq[right])
            water += right_max - seq[right]
            right -= 1

    return water

def trapRainWater(heights):

    stack, trapped_water = [], 0

    for hi_index, height in enumerate(heights):

        while stack and height >= heights[stack[-1]]:
            ground_height = heights[stack.pop()]
            if not stack:
                 continue
            lo_index = stack[-1]
            water_line = min(heights[lo_index], height)
            trapped_water += (water_line - ground_height) * (hi_index - lo_index - 1)

        stack.append(hi_index)

    return trapped_water

if __name__ == "__main__":
    seq = [2, 0, 1, 4, 0, 2, 5, 0, 7, 0, 3]
    print(trapRainWater(seq))