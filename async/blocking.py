import time

def cook_ramen():
    print('라면 물 끓이기 시작')

    time.sleep(3) # 3초동안 스레드 정지

    print('보글보글')

if __name__ == '__main__':
    print('요리 시작!')

    cook_ramen()
    
    print('다음작업 수행!')
