# protable

## protable的最小组成部分

- columns：他的作用是说明表格有哪些列，并且说明每一列的列名(对外显示的名称)和显示的字段(从代码中获取的数据)。
- rowkey：说明每一个数据的主键是什么。
- dataSource：赋值每行的数据。
    - 直接赋值
    - 请求赋值

## protable中最基本的功能

1. 排序功能：sorter：true.
2. 字体大小：通过设置classname，然后再css中设置字体大小即可.
3. 省略：如果超出文字限制，用省略号代替，当鼠标移上去时显示完整的数据，ellipsis: false/true.
4. 自动换行：
   1. 通过设置css中的white-space: normal !important;来自动换行。
   2. 通过直接在columns中加入 ` render: (_, row) => (<div style={{ whiteSpace: 'normal' }}>{row.desc}</div>) `来实现
5. 列宽度：width
6. 对其方式：align

![alt text](<屏幕截图 2025-11-15 200719.png>)

[code](code)