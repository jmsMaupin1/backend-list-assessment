#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
# Hint: Don't use `set()`


def remove_adjacent(nums):
    stack = []
    current = None
    for num in nums:
        if not current or num != current:
            stack.append(num)
            current = num
    
    return stack


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# The solution should work in "linear" time, making a single pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not linear time.
def linear_merge(list1, list2):
    l1_pointer = 0
    l2_pointer = 0
    list1_length = len(list1)
    list2_length = len(list2)
    total_list_length = list1_length + list2_length

    merged_list = []

    while l1_pointer + l2_pointer < total_list_length:
        if l1_pointer == list1_length:
            merged_list = merged_list + list2[l2_pointer:]
            break
        elif l2_pointer == list2_length:
            merged_list = merged_list + list1[l1_pointer:]
            break
        else:
            current_list1 = list1[l1_pointer]
            current_list2 = list2[l2_pointer]

            if current_list1 < current_list2:
                merged_list.append(current_list1)
                l1_pointer += 1
            else:
                merged_list.append(current_list2)
                l2_pointer += 1
    
    return merged_list



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    test(remove_adjacent([2, 2, 3, 3, 3, 4, 5, 2, 3]), [2, 3, 4, 5, 2, 3])

    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


# Standard boilerplate (python idiom) to call the main() function.
if __name__ == '__main__':
    main()
