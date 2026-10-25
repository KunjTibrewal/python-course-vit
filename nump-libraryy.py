import numpy as np
a = np.array([10, 20, 30, 40, 50])
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a)                       # [10 20 30 40 50]
print(b)                       # [[1 2 3]
                               #  [4 5 6]]
print(a[0])                    # 10
print(a[0:5:2])                # [10 30 50]
print(a.shape)                 # (5,)
print(b.shape)                 # (2, 3)
print(a.ndim)                  # 1
print(b.ndim)                  # 2
print(a.size)                  # 5
print(a.dtype)                 # int64 or int32 (system dependent)
print(a.astype(float))         # [10. 20. 30. 40. 50.]
print(a.reshape(5, 1))         # [[10]
                               #  [20]
                               #  [30]
                               #  [40]
                               #  [50]]
print(np.zeros(4))             # [0. 0. 0. 0.]
print(np.ones(3))              # [1. 1. 1.]
print(np.arange(1, 6))          # [1 2 3 4 5]
print(np.arange(0, 10, 2))      # [0 2 4 6 8]
print(np.linspace(0, 10, 5))    # [ 0.   2.5  5.   7.5 10. ]
print(np.sum(a))               # 150
print(np.mean(a))              # 30.0
print(np.max(a))               # 50
print(np.min(a))               # 10
print(np.argmax(a))            # 4 (index of maximum element)
print(np.argmin(a))            # 0 (index of minimum element)
print(np.sort(a[::-1]))        # [10 20 30 40 50]
print(a + 5)                   # [15 25 35 45 55]
print(a * 2)                   # [20 40 60 80 100]
print(a ** 2)                  # [100 400 900 1600 2500]
print(a > 25)                  # [False False  True  True  True]
print(a[a > 25])               # [30 40 50]
print(b[0])                    # [1 2 3]
print(b[0, 1])                 # 2
print(b[:, 0])                 # [1 4]
print(b[0, :])                 # [1 2 3]
print(b.T)                     # [[1 4]
                               #  [2 5]
                               #  [3 6]]
print(np.sum(b))               # 21
print(np.sum(b, axis=0))       # [5 7 9]
print(np.sum(b, axis=1))       # [ 6 15]
print(np.concatenate((a, a)))  # [10 20 30 40 50 10 20 30 40 50]
print(np.unique([1, 2, 2, 3, 3, 3]))
                               # [1 2 3]
print(np.sqrt([4, 9, 16]))     # [2. 3. 4.]
print(np.where(a > 25))        # (array([2, 3, 4]),)
c = np.full((3, 3), 1)
d = np.eye(3)
print(c@d)                    # [[1. 1. 1.]
                              #  [1. 1. 1.]
                              #  [1. 1. 1.]]
e = np.array([1, 2, 3])
f = np.array([4, 5, 6])
print(np.dot(e, f))           # 32