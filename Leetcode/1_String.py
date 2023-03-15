'''1.Valid-Palindrome'''
# Case_1 -> Use isalnum() , strs.pop(0) vs strs.pop() 
class Solution:
    def isPalindrome(self, s):
        strs = []
        for char in s:
            if char.isalnum():
            # isalnum() -> number, word verify function
                strs.append(char.lower()) # all lowercase

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                # first value of list != last value of list
                # pop(index)
                return False
        return True
    
# Case_2 -> Use Deque (양방향 Queue) -> O(1) , push & pop 이 빈번한 알고리즘에서 사용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
    
# deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
# deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
# deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
# deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
# deque.remove(item): item을 데크에서 찾아 삭제한다.
# deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

# Case_3 -> 정규식(전처리)으로 필터링 이후 슬라이싱 사용 -> 전처리 학습
class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s) # a-z : 알파벳 전부, 0-9 : 숫자 전부, ^ : Not
        
        return s == s[::-1]
    

'''2.reverse-string'''

# Case_1 : use_two_pointer(범위를 좁혀가면서)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s)-1

        while left< right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        print(s)
# Case_2 : use_reverse()
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

        print(s)

'''3. reorder-data-in-log-files '''

# Case_01 : use_lambda

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # lambda (variable .. : expression) & map, filter also
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 1: -> 식별자를 제외한 strs

        return letters + digits
'''4. most-common-word'''
# Case_01 : List_Comprehension, Counter -> data: count 형태의 dict로 return 하는 함수
# 정규식 사용 ^\w : 문자가 아닌 것을 '' 로 치환 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                if word not in banned]
        counts = collections.Counter(words)
        
        return counts.most_common(1)[0][0]
'''5. group-anagrams'''
# anagrams : 언어유희, for example) 문전박대 -> 대박전문

# Case_01 : 정렬하여 딕셔너리에 추가
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) # key값의 오류가 발생하지 않도록
        
        for char in strs:
            anagrams[''.join(sorted(char))].append(char)
        return anagrams.values()


    
    
    
# More Study: List_Comprehension, Deque, lambda(filter,map), counter, defaultdict(also collections), split, join, sorted & sort, 

# 1. List Comprehension : [expression for variable in list]

# [표현식 for 변수 in 리스트] -> [n*n for n in array]
# [표현식 for 변수 in 리스트 조건문] -> [n for n in range(20) if n%2 == 0]
# [표현식 if 조건 else 표현식 for 변수 in 리스트] -> [n if n > 0 else 0 for n in array ]



# 2-0 collections (container형 자료형)

# namedtuple(): 이름 붙은 필드를 갖는 튜플 서브 클래스를 만들기 위한 팩토리 함수
# deque: 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너
# ChainMap: 여러 매핑의 단일 뷰를 만드는 딕셔너리류 클래스
# Counter: 해시 가능한 객체를 세는 데 사용하는 딕셔너리 서브 클래스 -> key: value = 값 : 개수
# OrderedDict: 항목이 추가된 순서를 기억하는 딕셔너리 서브 클래스
# defaultdict: 누락된 값을 제공하기 위해 팩토리 함수를 호출하는 딕셔너리 서브 클래스 -> key가 없어도 오류 x
# UserDict: 더 쉬운 딕셔너리 서브 클래싱을 위해 딕셔너리 객체를 감싸는 래퍼
# UserList: 더 쉬운 리스트 서브 클래싱을 위해 리스트 객체를 감싸는 래퍼
# UserString: 더 쉬운 문자열 서브 클래싱을 위해 문자열 객체를 감싸는 래퍼

