import time
import copy

class Sort:
    def init(self):
        self.mother_list = []


    # setting random list
    def setting(self, rand_list):
        self.mother_list = copy.deepcopy(rand_list)
        # create right answer
        self.right_answer = sorted(self.mother_list)


    # sequential #1 sort
    def sequential_1(self):
        # copy random list
        sequential_list_1 = copy.deepcopy(self.mother_list)
        # start timewatch
        sequential_1_starttime = time.time()
        # count reset
        change_count = 0
        # sort
        for i in range(0, len(sequential_list_1)):
            for j in range(i+1, len(sequential_list_1)):
                if sequential_list_1[i] > sequential_list_1[j]:
                    sequential_list_1[i], sequential_list_1[j] = sequential_list_1[j], sequential_list_1[i]
                    change_count += 1
        # end timewatch
        sequential_1_endtime = time.time()
        # sequential #1 result
        print("==========")
        print("순차정렬 #1 완료")
        print("소요시간 {time}초".format(time = sequential_1_endtime - sequential_1_starttime))
        if(sequential_list_1 == self.right_answer):
            print("정상작동 확인")
            print("교체 횟수: {times}회".format(times = change_count))
        else:
            print("정상작동 실패")
            print("차이 내용")
            print(sequential_list_1)
            print(self.right_answer)


    # bubble #1 sort
    def bubble_1(self):
        # copy random list
        bubble_list_1 = copy.deepcopy(self.mother_list)
        # start timewatch
        bubble_1_starttime = time.time()
        # count reset
        change_count = 0
        # sort
        for i in range(len(bubble_list_1), 0, -1):
            for j in range(0, i-1):
                if bubble_list_1[j] > bubble_list_1[j+1]:
                    bubble_list_1[j], bubble_list_1[j+1] = bubble_list_1[j+1], bubble_list_1[j]
                    change_count += 1

        # end timewatch
        bubble_1_endtime = time.time()
        # sequential #1 result
        print("==========")
        print("버블정렬 #1 완료")
        print("소요시간 {time}초".format(time = bubble_1_endtime - bubble_1_starttime))
        if(bubble_list_1 == self.right_answer):
            print("정상작동 확인")
            print("교체 횟수: {times}회".format(times = change_count))
        else:
            print("정상작동 실패")
            print("차이 내용")
            print("정답")
            print(self.right_answer)
            print("정렬결과")
            print(bubble_list_1)
 

    # selection sort #1 sort
    def selection_1(self):
        # copy random list
        selection_list_1 = copy.deepcopy(self.mother_list)
        # start timewatch
        selection_starttime = time.time()
        # count reset
        change_count = 0
        # sort
        for i in range(0, len(selection_list_1)):
            temp_list = []
            for j in range(i+1, len(selection_list_1)):
                temp_list.append(selection_list_1[j])
                if selection_list_1[i] > min(temp_list):
                    selection_list_1[i], selection_list_1[j] = selection_list_1[j], selection_list_1[i]
                    change_count += 1
        # end timewatch
        selection_endtime = time.time()
        # selection #1 result
        print("==========")
        print("선택정렬 #1 완료")
        print("소요시간 {time}초".format(time = selection_endtime - selection_starttime))
        if(selection_list_1 == self.right_answer):
            print("정상작동 확인")
            print("교체 횟수: {times}회".format(times = change_count))
        else:
            print("정상작동 실패")
            print("차이 내용")
            print(selection_list_1)
            print(self.right_answer)
 

    # insertion sort #1 sort
    def insertion_1(self):
        # copy random list
        insertion_list_1 = copy.deepcopy(self.mother_list)
        # start timewatch
        insertion_starttime = time.time()
        # count reset
        change_count = 0
        # sort
        for i in range(0, len(insertion_list_1)):
            while 0 < i and insertion_list_1[i] < insertion_list_1[i - 1]: 
                insertion_list_1[i], insertion_list_1[i - 1] = insertion_list_1[i - 1], insertion_list_1[i]
                i -= 1
                change_count += 1
        # end timewatch
        insertion_endtime = time.time()
        # insertion #1 result
        print("==========")
        print("삽입정렬 #1 완료")
        print("소요시간 {time}초".format(time = insertion_endtime - insertion_starttime))
        if(insertion_list_1 == self.right_answer):
            print("정상작동 확인")
            print("교체 횟수: {times}회".format(times = change_count))
        else:
            print("정상작동 실패")
            print("차이 내용")
            print(insertion_list_1)
            print(self.right_answer)
