{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "40071985",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0보다 크고 99보다 작은 정수를 입력하세요\n",
      "num : -1\n",
      "0보다 크고 99보다 작은 정수를 입력하세요\n",
      "num : 100\n",
      "0보다 크고 99보다 작은 정수를 입력하세요\n",
      "num : 55\n",
      "알고리즘 사이클 길이 : 3\n"
     ]
    }
   ],
   "source": [
    "# 브론즈 1 - 1110번\n",
    "'''\n",
    "0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.\n",
    "먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.\n",
    "그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면\n",
    "새로운 수를 만들 수 있다. \n",
    "\n",
    "다음 예를 보자.\n",
    "26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.\n",
    "위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.\n",
    "N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.\n",
    "'''\n",
    "\n",
    "while True:\n",
    "    \n",
    "    print('0보다 크고 99보다 작은 정수를 입력하세요')\n",
    "    \n",
    "    inital_n = int(input('num : ')) \n",
    "    \n",
    "    cheak_n = inital_n # 마자믹 확인 용\n",
    "    \n",
    "    #0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때\n",
    "    if inital_n >= 0 and inital_n <= 99:\n",
    "        \n",
    "        break\n",
    "\n",
    "# 사이클 길이\n",
    "count_num = 0\n",
    "        \n",
    "while True:\n",
    "    \n",
    "    count_num += 1\n",
    "    \n",
    "    # 주어진 수가 10보다 작다면   \n",
    "    if inital_n < 10: # 5\n",
    "\n",
    "        # 앞에 0을 붙여 두 자리 수로 만들고\n",
    "        n = '0' + str(inital_n)\n",
    "\n",
    "    else:\n",
    "\n",
    "        n = str(inital_n) \n",
    "\n",
    "    n_first = n[0] \n",
    "    n_last = n[-1] \n",
    "    \n",
    "    # 각 자리의 숫자를 더한다\n",
    "    new_plus = int(n_first) + int(n_last) # 10 # 5\n",
    "\n",
    "    # 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙임\n",
    "    new_n = n_last + str(new_plus)[-1] \n",
    "\n",
    "    inital_n = int(new_n)\n",
    "    \n",
    "    # 주어진 숫자와 결과값이 같은 지 확인\n",
    "    if cheak_n == inital_n: \n",
    "        break\n",
    "        \n",
    "        \n",
    "print(f'알고리즘 사이클 길이 : {count_num}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "99148893",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Englsh : Mississipi\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{0: 1, 1: 4, 2: 4, 8: 1}"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 브론즈 1 - 1157번\n",
    "\n",
    "'''\n",
    "알파벳 대소문자로 된 단어가 주어지면,\n",
    "이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.\n",
    "단, 대문자와 소문자를 구분하지 않는다.\n",
    "'''\n",
    "\n",
    "word = str(input('Englsh : '))\n",
    "\n",
    "word = word.lower()\n",
    "\n",
    "orgin_word = list(word)\n",
    "list_word = list(word)\n",
    "\n",
    "dict_count = {}\n",
    "\n",
    "for i in range(len(list_word)): # 0\n",
    "    \n",
    "    count_num = 0\n",
    "    \n",
    "    if list_word[i] != None:\n",
    "        \n",
    "        count_num += 1\n",
    "    \n",
    "        for j in range(i+1, len(list_word)): # 1 ~\n",
    "\n",
    "            if list_word[i] == list_word[j]:\n",
    "\n",
    "                count_num += 1\n",
    "\n",
    "                list_word[j] = None\n",
    "\n",
    "        dict_count[i] = count_num\n",
    "        \n",
    "    else:\n",
    "        pass\n",
    "    \n",
    "    \n",
    "list_key = list(dict_count.keys())\n",
    "\n",
    "list\n",
    "\n",
    "        \n",
    "        \n",
    "\n",
    "\n",
    "\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "c5f9179e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'i']"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 'Mississipi'\n",
    "list(a.lower())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "962267e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 8]"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dict_count = {0: 1, 1: 4, 2: 4, 8: 1}\n",
    "\n",
    "lst_key = list(dict_count.keys())\n",
    "lst_key"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "a71d080c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for i in range(len(lst_key)):\n",
    "    if dict_count[lst_key[i]] < dict_count[lst_key[i+1]]:\n",
    "        max_key = lst_key[i+1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "efbea558",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea3e051a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
