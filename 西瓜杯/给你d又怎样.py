from Crypto.Util.number import *
from gmpy2 import *


def get_factors(list_a):
    prime_factors = [
        2,
        3,
        13,
        107,
        193,
        409,
        2131,
        7817,
        822953723815903,
        20203567811678085259,
        28480348970588539667342897711,
    ]
    p = 1
    for i in range(11):
        p = p * (prime_factors[i] ** (list_a[i]))
    return p


def generate_lists(input_list, current_list=None, index=0):
    if current_list is None:
        current_list = []

    if index == len(input_list):
        return [current_list]

    results = []
    for i in range(input_list[index] + 1):  # 修改这里，允许等于
        results += generate_lists(input_list, current_list + [i], index + 1)

    return results


e = 65537
hint = 7680157534215495795423318554486996424970862185001934572714615456147511225105
c = 48794779998818255539069127767619606491113391594501378173579539128476862598083
d = 45673813678816865674850575264609274229013439838298838024467777157494920800897
phi = e * d - 1
print(phi)  # 计算原本的(p-1)*(q-1),分解后得到以下质因数，其中2有7个，3有3个
prime_factors = [
    2,
    3,
    13,
    107,
    193,
    409,
    2131,
    7817,
    822953723815903,
    20203567811678085259,
    28480348970588539667342897711,
]
factor = []
factors_list = generate_lists(
    [7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
)  # 生成所有质因数可能的次数(实现方法有些丑陋)
for i in factors_list:
    factor.append(get_factors(i))  # 生成所有phi的因数
a = 0
for i in factor:  # 遍历所有因数，计算hint值看是否等于给出的hint
    a = a + 1
    print(a)  # 计数器，查看进度用，在7840hs上跑了大约10mins得到结果
    for j in factor:
        n = (i + 1) * (j + 1)
        if (
            pow(n, e, c)
            == 7680157534215495795423318554486996424970862185001934572714615456147511225105
        ):
            print(long_to_bytes(pow(c, d, n)))  # 得出n后即可直接计算
