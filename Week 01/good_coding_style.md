# coding style 
    1.二元运算符号两边加空格，单元不加空格 eg. a + b, i++
    2.（）和 {} 要加空格在 if 后 eg. if (a==b) :
    3. 空行分开逻辑块
    4. 逗号后面加空格 eg.  left, right = 2, 3

# readability
    1.变量名用单词表示
    2.一个函数内部不超过三层 indention
    3.多用子函数来减少入口函数代码量
    4.多用 continue， 少用 if

# bug free 
    1.入口函数的参数进行异常检测 
    2.访问index时，保证index不会越界
    3.访问一个对象的属性或者方法时，一定要确保这个对象不是空
    4.不用全局变量