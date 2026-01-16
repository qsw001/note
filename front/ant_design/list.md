# Ant Design —— List 组件使用说明（实战向）

## 一、List 是什么？

List 是 Ant Design 提供的列表组件，用于渲染一组结构相同的数据。

常见使用场景：

- Todo 列表
- 评论列表
- 用户列表
- 消息列表

List 只负责结构 + 样式，不负责任何业务逻辑。

## 二、最基础用法

```tsx
import { List } from "antd";

const data = ["任务一", "任务二", "任务三"];

<List
  dataSource={data}
  renderItem={(item) => <List.Item>{item}</List.Item>}
/>
```

核心属性说明

| 属性 | 作用 |
| --- | --- |
| dataSource | 列表数据（数组） |
| renderItem | 定义“每一项如何渲染” |
| List.Item | 单条列表项容器 |

## 三、renderItem 是什么？

```tsx
(item) => <List.Item>{item}</List.Item>
```

含义：

- 接收数组中的一项数据，返回 JSX 组件

等价于：

```tsx
function renderItem(item) {
  return <List.Item>{item}</List.Item>;
}
```

## 四、Todo 场景下的标准写法（重点）

数据结构示例

```ts
{
  id: 1,
  text: "学习 React",
  done: false
}
```

推荐写法

```tsx
<List
  dataSource={todos}
  renderItem={(todo) => (
    <List.Item
      key={todo.id}
      actions={[
        <a onClick={() => handleDelete(todo.id)}>删除</a>
      ]}
    >
      {todo.text}
    </List.Item>
  )}
/>
```

关键规范

- `key` 必须放在 `List.Item` 上
- List / Item 不保存 state
- 删除逻辑在父组件（App）中处理

## 五、List.Item 的常用能力

### 1. actions（右侧操作区）

```tsx
<List.Item
  actions={[
    <a>编辑</a>,
    <a>删除</a>,
  ]}
>
  内容
</List.Item>
```

特点：

- 自动右对齐
- 不用写 CSS

### 2. extra（右侧扩展内容）

```tsx
<List.Item extra={<img src="cover.png" width={80} />}>
  内容
</List.Item>
```

适合：

- 图片
- 状态展示

### 3. List.Item.Meta（结构化内容）

```tsx
<List.Item>
  <List.Item.Meta
    title="学习 React"
    description="完成 Todo List"
  />
</List.Item>
```

适合：

- 标题 + 描述
- 评论 / 用户信息

## 六、空数据与加载状态

空列表文案

```tsx
<List
  dataSource={todos}
  locale={{ emptyText: "暂无数据" }}
/>
```

loading 状态

```tsx
<List
  loading={loading}
  dataSource={todos}
/>
```

## 七、List vs map（工程角度）

map 写法

```tsx
todos.map(todo => <div>{todo.text}</div>)
```

List 的优势

- 内置布局与分割线
- 支持 loading / empty
- actions / extra / meta
- UI 风格统一（后台系统首选）

练习可以 map，项目优先 List。

## 八、与 Todo 组件拆分的关系

```
App（state）
 └─ TodoList
     └─ List
         └─ List.Item（TodoItem）
```

- App：管理 state
- TodoList：渲染列表
- TodoItem：纯展示 + 事件上抛

## 九、常见错误（必须避免）

- ❌ 在 List.Item 中直接修改 state
- ❌ 在 Item 内部写删除逻辑
- ❌ 忘记 key
- ❌ 依赖 index 作为 key

## 十、一句话总结

List = 列表结构与样式工具，业务逻辑永远属于你自己。

如果你需要，我可以下一步直接给你生成：

- TodoList.tsx 标准模板
- React + antd Todo 项目完整 md 讲义版
