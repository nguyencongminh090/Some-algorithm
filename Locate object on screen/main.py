import pyautogui
import keyboard
import time
from concurrent.futures import ThreadPoolExecutor  # Đa luồng

def prunning(arr):
    # Cắt tỉa vị trí trùng lặp
    count_p = 0
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if i == j:
                continue
            try:
                if (abs(arr[i][0] - arr[j][0]) < 20 and arr[i][0] - arr[j][0] != 0) and abs(arr[i][1] - arr[j][1]) < 5:
                    arr.pop(j)
                    count_p += 1
                if (abs(arr[i][1] - arr[j][1]) < 20 and arr[i][1] - arr[j][1] != 0) and abs(arr[i][0] - arr[j][0]) < 5:
                    arr.pop(j)
                    count_p += 1
            except:
                continue
    return arr, count_p

def process(func, arr):
  executor = ThreadPoolExecutor(max_workers=5)
  future = executor.submit(func, arr)
  return future.result()

def get_opening():
    coord_b = []
    coord_w = []
    for pos in pyautogui.locateAllOnScreen('PO\\black.png', confidence=0.9):
        position = (pos[0] + pos[2] // 2, pos[1] + pos[3] // 2)
        coord_b.append(position)

    for pos in pyautogui.locateAllOnScreen('PO\\white.png', confidence=0.9):
        position = (pos[0] + pos[2] // 2, pos[1] + pos[3] // 2)
        coord_w.append(position)
    def t1(coord_w):
        # Cắt tỉa những vị trí trùng lặp
        while prunning(coord_w)[1] != 0:
            coord_w = prunning(coord_w)[0]
        return coord_w
    def t2(coord_b):
        # Cắt tỉa những vị trí trùng lặp
        while prunning(coord_b)[1] != 0:
            coord_b = prunning(coord_b)[0]
        return coord_b
    # Xử lý song song
    coord_w = process(t1, coord_w)
    coord_b = process(t2, coord_b)
    try:
        x,y = pyautogui.locateCenterOnScreen('PO\\ccc.png', confidence=0.7)
        coord_b.append((x, y))
    except:
        x, y = pyautogui.locateCenterOnScreen('PO\\wht.png', confidence=0.8)
        coord_w.append((x, y))
    return coord_b, coord_w


def opening():
    a = time.perf_counter()
    black = get_opening()[0]
    white = get_opening()[1]
    output = []
    b = time.perf_counter()
    
##    if len(black) > len(white):
##        print('Computer play white')
##    else:
##        print('Computer play black')
##    print('Report')
##    print('Runtime: %.2f sec' % (b-a))
##    print('Speed: {} move/sec'.format(round((b-a)/max(len(black), len(white)), 2)))
##    print(len(black))
    
    for i in range(len(max(black, white))*2):
        try:
            output.append(black[i])
            output.append(white[i])
        except:
            break
    return output
