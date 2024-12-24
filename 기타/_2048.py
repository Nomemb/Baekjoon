import copy

N = list(map(int, input().split()))[0]
MAX_VAL = 0
data_array = []
for i in range(N):
    data_array.append(list(map(int, input().split())))


def move_left(data):
    global MAX_VAL
    for line_num in range(N):
        prior_val = None
        line_result = []
        data[line_num].append(None)
        for row_val in data[line_num]:
            if row_val == 0:
                pass
            else:
                if prior_val == row_val and row_val is not None:
                    new_val = prior_val + row_val
                    if MAX_VAL < new_val:
                        MAX_VAL = new_val
                        print(MAX_VAL)
                    line_result.append(new_val)
                    prior_val = None

                    if prior_val is not None:
                        if MAX_VAL < prior_val:
                            MAX_VAL = prior_val
                        line_result.append(prior_val)
                        prior_val = row_val
            if len(line_result) == N:
                data[line_num] = line_result
            else:
                while len(line_result) < N:
                    line_result.append(0)
                data[line_num] = line_result
    return data


def move_step(data):
    def _left(data):
        # copy
        data = copy.deepcopy(data)

        # move left
        data = move_left(data)

        return data

    def _right(data):
        # copy
        data = copy.deepcopy(data)

        # reverse
        for line_num in range(N):
            data[line_num] = data[line_num][::-1]

        # move left
        data = move_left(data)

        # reverse
        for line_num in range(N):
            data[line_num] = data[line_num][::-1]

        return data

    def _up(data):
        # rotate
        data = [[data[row_num][line_num] for row_num in range(N)] for line_num in range(N)]

        # move left
        data = move_left(data)

        # rotate
        data = [[data[row_num][line_num] for row_num in range(N)] for line_num in range(N)]

        return data

    def _down(data):
        # rotate & reverse
        data = [[data[row_num][line_num] for row_num in range(N)] for line_num in range(N)]
        for line_num in range(N):
            data[line_num] = data[line_num][::-1]

        # move left
        data = move_left(data)

        # rotate & reverse
        for line_num in range(N):
            data[line_num] = data[line_num][::-1]
        data = [[data[row_num][line_num] for row_num in range(N)] for line_num in range(N)]

        return data

    return _left(data), _right(data), _up(data), _down(data)


results = [data_array, ]
for _ in range(5):
    _results, results = results, []
    for data in _results:
        for result in move_step(data):
            results.append(result)

print(MAX_VAL)
