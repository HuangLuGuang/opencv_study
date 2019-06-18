# -*- coding: utf-8 -*-
# @createTime    : 2019/6/18 13:38
# @author  : Huanglg
# @fileName: 02_数据类型.py
# @email: luguang.huang@mabotech.com
import numpy as np

dt = np.dtype(np.int32)

dt = np.dtype("i4") # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替

dt = np.dtype([("age", np.int8)])

student = np.dtype([("name", "S20"), ("age", "i1"), ("marks", "f4")])

a = np.array([(10,), (20,), (30,)], dtype=dt)
s = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(s)
print(s['name'])
