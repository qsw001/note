# Ant Design · Typography 笔记

## 1. Typography 是什么？

**Typography（排版）** 是 Ant Design 提供的一套**文字展示组件体系**，用于统一管理：

- 标题
- 正文
- 说明文字
- 强调 / 状态文本

本质：**用组件而不是原生 HTML 标签来显示文字**。

---

## 2. 为什么要用 Typography？

不用 Typography 时常见问题：

- 样式分散（`h1 / p / span + style`）
- 字号、行高、颜色不统一
- 后期改设计成本高

Typography 的作用：

- 统一文字规范
- 自带功能（复制 / 省略 / 编辑）
- 支持主题定制（ConfigProvider）

---

## 3. 基本用法（统一写法）

使用前要先解构赋值

```js
import { Typography } from "antd";
const { Title, Text, Paragraph } = Typography;
```

## 4. Title

用于页面或模块标题。

```js
<Title level={1}>一级标题</Title>
<Title level={2}>二级标题</Title>
<Title level={3}>三级标题</Title>
```

level类似于h1,h2；取值范围为1-5

## 5. Text（行内文本）

用于普通文本、强调文本、状态文本。

```js
<Text>普通文本</Text>
<Text type="secondary">次要文本</Text>
<Text type="success">成功文本</Text>
<Text type="warning">警告文本</Text>
<Text type="danger">危险文本</Text>
<Text strong>加粗文本</Text>
```

## 6. Paragraph（段落）

用于多行说明性文字。

```js
<Paragraph>
  这是一个段落文本，适合多行说明内容。
</Paragraph>
```
特点：
- 自动处理行高和段间距
- 比原生 p 标签更统一

## 7. 常用增强功能
7.1 文本复制
```<Text copyable>可复制内容</Text>```

7.2 文本省略（ellipsis）
```js
<Paragraph ellipsis={{ rows: 2 }}>
  这是一段很长很长的文本……
</Paragraph>
```

7.3 可编辑文本
```js
<Paragraph editable>点击即可编辑</Paragraph>
```