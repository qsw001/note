# Ant Design · Input 笔记

## 1. Input 是什么？

**Input** 是 Ant Design 提供的**文本输入组件**，用于接收用户输入的字符串数据。

主要用途：
- 表单输入
- 搜索框
- 用户名 / 密码输入
- 备注、描述填写

本质：**Input 是用户输入数据的入口组件**。

---

## 2. 最基本用法

```js
import { Input } from "antd";

function App() {
  return <Input placeholder="请输入内容" />;
}
```

## 3. 受控组件
3.1 什么是受控组件？

受控组件指的是：
Input 的显示值完全由 React 的 state 控制。

```js
import { Input } from "antd";
import { useState } from "react";

function App() {
  const [value, setValue] = useState("");

  return (
    <Input
      value={value}
      onChange={e => setValue(e.target.value)}
    />
  );
}
```

核心要点：
- value 决定输入框显示的内容
- onChange 决定如何更新状态
- state 是唯一数据源

3.2 不受控用法（不推荐）
<Input defaultValue="hello" />

说明：只在初始渲染时生效后续变化不由 React 管理不适合复杂表单

## 4. 常用属性
4.1 placeholder（占位提示）
<Input placeholder="请输入用户名" />

4.2 disabled（禁用）
<Input disabled />

4.3 allowClear（一键清空）
<Input allowClear />

4.4 maxLength（最大长度）
<Input maxLength={20} />

4.5 showCount（字符统计）
<Input maxLength={20} showCount />

## 5. 前后缀（prefix / suffix）
<Input
  prefix="@"
  suffix=".com"
  placeholder="邮箱"
/>


常见使用场景：

- 邮箱输入
- 金额输入
- 搜索框

## 6. Input 的常见变体
6.1 密码输入框
```js
<Input.Password placeholder="请输入密码" />
```
特点：

- 自带显示 / 隐藏功能
- 不需要额外逻辑

6.2 多行文本输入
```js
<Input.TextArea rows={4} />
```
常用于：备注,描述,评论

6.3 搜索框
```js
<Input.Search
  placeholder="搜索"
  onSearch={value => console.log(value)}
/>
```

特点：支持回车触发,自带搜索按钮

## 7. 常用事件
7.1 onChange
<Input onChange={e => console.log(e.target.value)} />

说明：

- e 是事件对象
- e.target.value 是当前输入值

7.2 onPressEnter
<Input onPressEnter={() => submit()} />

## 8. 与 Form 结合使用
import { Form, Input } from "antd";

```js
<Form>
  <Form.Item name="username" label="用户名">
    <Input />
  </Form.Item>
</Form>
```

## 一句话总结

Input 是 Ant Design 提供的文本输入组件，通常以受控组件方式使用，通过 value 和 onChange 与 React 状态绑定，用于构建表单和用户输入交互。