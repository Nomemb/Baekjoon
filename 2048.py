import copy

N = list(map(int, input().split()))[0]

data_array = []
MAX_VAL = 0
for i in range(N):
    data_array.append(list(map(int, input().split())))
    MAX_VAL = max(MAX_VAL, max(data_array[i]))


def move_data(_data):
    def up(_data):
        global MAX_VAL
        _data = copy.deepcopy(_data)
        for i in range(N):
            for j in range(N - 1):
                if _data[j][i] == 0:
                    for w in range(j + 1, N):
                        if _data[w][i] != 0:
                            _data[j][i], _data[w][i] = _data[w][i], 0
                            break

                for w in range(j + 1, N):
                    if _data[w][i] != 0 and _data[j][i] != data[w][i]:
                        break
                    if _data[j][i] == _data[w][i]:
                        _data[j][i], _data[w][i] = _data[j][i] * 2, 0
                        if MAX_VAL < _data[j][i]: MAX_VAL = _data[j][i]
                        break
        return _data

    def down(_data):
        global MAX_VAL
        _data = copy.deepcopy(_data)

        for i in range(N - 1, -1, -1):
            for j in range(N - 1, 0, -1):
                if _data[j][i] == 0:
                    for w in range(j - 1, -1, -1):
                        if _data[w][i] != 0:
                            _data[j][i], _data[w][i] = _data[w][i], 0
                            break

                for w in range(j - 1, -1, -1):
                    if _data[w][i] != 0 and _data[j][i] != _data[w][i]:
                        break
                    if _data[j][i] == _data[w][i]:
                        _data[j][i], _data[w][i] = _data[j][i] * 2, 0
                        if MAX_VAL < _data[j][i]: MAX_VAL = _data[j][i]
                        break
        return _data

    def left(_data):
        global MAX_VAL
        _data = copy.deepcopy(_data)

        for i in range(N):
            for j in range(N - 1):
                if _data[i][j] == 0:
                    for w in range(j + 1, N):
                        if _data[i][w] != 0:
                            _data[i][j], _data[i][w] = _data[i][w], 0
                            break

                for w in range(j + 1, N):
                    if _data[i][w] != 0 and _data[i][j] != data[i][w]:
                        break
                    if _data[i][j] == _data[i][w]:
                        _data[i][j], _data[i][w] = _data[i][j] * 2, 0
                        if MAX_VAL < _data[i][j]: MAX_VAL = _data[i][j]
                        break
        return _data

    def right(_data):
        global MAX_VAL
        _data = copy.deepcopy(_data)

        for i in range(N - 1, -1, -1):
            for j in range(N - 1, 0, -1):
                if _data[i][j] == 0:
                    for w in range(j - 1, -1, -1):
                        if _data[i][w] != 0:
                            _data[i][j], _data[i][w] = _data[i][w], 0
                            break

                for w in range(j - 1, -1, -1):
                    if _data[i][w] != 0 and _data[i][j] != _data[i][w]:
                        break
                    if _data[i][j] == _data[i][w]:
                        _data[i][j], _data[i][w] = _data[i][j] * 2, 0
                        if MAX_VAL < _data[i][j]: MAX_VAL = _data[i][j]
                        break
        return _data

    return up(_data), down(_data), left(_data), right(_data)


results = [data_array, ]
for _ in range(5):
    _results, results = results, []
    for data in _results:
        for result in move_data(data):
            results.append(result)

print(MAX_VAL)
