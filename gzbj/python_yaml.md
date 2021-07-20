# Python3操作YAML文件

## 数据及配置文件

数据及文件通常有三种类型：

1. 配置文件型：如ini，conf，properties文件，适合存储简单变量和配置项，最多支持两层，不适合存储多层嵌套数据
2. 表格矩阵型：如csv，excel等，适合于存储大量同类数据，不适合存储层级结构的数据
3. 多层嵌套型：如XML，HTMl，JSON、YAML，TOML等，适合存储单条或少数多层嵌套数据，不适合存储大量数据

YAML兼容JSON格式，简洁，强大，灵活，可以很方便的构造层级数据并快速转为Python中的字典。

## YAML简介

YAML（YAML Ain't Markup Language）即一种反标记（XML）语言。强调数据为中心，而非标记。YAML大小写敏感，使用缩进代表层级关系。
YAML中支持对象Object(对应Python中的字典), 数组Array(对应Python中的列表)以及常量（字符串、数字（int/float），true/false/null）。
相比于JSON格式，YAML免除了双引号，逗号，大括号，中括号等，（当然也支持原始的JSON格式），并且支持注释，类型转换，跨行，锚点，引用及插入等等。

### 基本格式

- 对象：使用`key: value`表示，**冒号后面有一个空格**，也可以是使用`{key: value}`（flow流格式）或`{"key": "value"}`表示
- 数组：使用`- value`表示，**-后面有一个空格**，每项一行，也可以使用`[value1,value2,value3,...]` （flow流格式）或`["value1", "value2", "value3", ...]`
- 字符串：`abc`或`"abc"`
- 数字：`123`或`123.45`
- true/false：`true`/`false`,`TRUE`/`FALSE`,`True`/`False`或`on`/`off`, `ON`/`OFF`, `On`/`Off`
- null: `null`,`NULL`, `Null`或`~`

示例文件`demo.yaml`:

```yaml
# 注释：示例yaml文件
name: Cactus
age: 18
skills: 
  -
    - Python
    - 3
  -
    - Java
    - 5
has_blog: true
gf: ~
```

相当于以下JSON格式

```json
{
  "name": "Cactus",
  "age": 18,
  "skills": [
    [
      "Python",
      3
    ],
    [
      "Java",
      5
    ]
  ],
  "has_blog": true,
  "gf": null
}
```

### 类型转换

使用`!!str`, `!!float`等可以将默认类型转为指定类型，如

```yaml
- !!float 3
- !!str 4
- !!str true
```

对应JSON格式

```json
[
  3.0,
  "4",
  "true"
]
```

### 多行文本及拼接

- `|` 保留多行文本（保留换行符）
- `>` 将多行拼接为一行

示例：

```yaml
a: |
  我
  喜欢你

b: >
  我
  不喜欢你
  才怪
```

对应JSON格式

```json
{
  "a": "我\n喜欢你\n",
  "b": "我 不喜欢你 才怪"
}
```

### 锚点，引用及插入

在`-`或`:`后 加上`&锚点名`为当前字段建立锚点，下面可使用`*锚点名`引用锚点，或使用`<<: *锚点名`直接将锚点数据插入到当前的数据中，示例如下：

```yaml
users:
  - &zs
    name: 张三
    password: !!str 123456
  - &ls
    name: 李四
    password: abcdefg

case1:
  login: *zs

case2:
  user:
    <<: *ls
    age: 20
```

对应JSON格式：

```json
{
  "users": [
    {
      "name": "张三",
      "password": "123456"
    },
    {
      "name": "李四",
      "password": "abcdefg"
    }
  ],
  "case1": {
    "login": {
      "name": "张三",
      "password": "123456"
    }
  },
  "case2": {
    "user": {
      "name": "李四",
      "password": "abcdefg",
      "age": 20
    }
  }
}
```

## Python操作YAML文件及字符串

> 需要安装pyyaml， `pip install pyyaml`

和JSON文件类似，yaml也提供load和dump两种方法。

- `yaml.load()`或`yaml.safe_load(YAML字符串或文件句柄)`：yaml -> 字典，如yaml中有中文，需要使用 `字符串.encode('utf-8')`或打开文件时指定`encoding='utf-8'`
- `yaml.dump(字典)`：默认为flow流格式，即字典`{b': {'c': 3, 'd': 4}}`，会被转为`b: {c: 3, d: 4}`形式，可以使用`default_flow_style=False`关闭流模式

> 由于`yaml.load()`支持原生Python对象，不安全，建议使用`yaml.safe_load()`

### 示例1：yaml字符串 -> 字典

```python
import yaml
yaml_str = '''
name: Cactus
age: 18
skills: 
  -
    - Python
    - 3
  -
    - Java
    - 5
has_blog: true
gf: ~
'''
print(yaml.safe_load(yaml_str)) 
```

打印结果：

```python
{'name': 'Cactus', 'age': 18, 'skills': [['Python', 3], ['Java', 5]], 'has_blog': True, 'gf': None}
```

> 如果有中文，可以使用`yaml.load(yaml_str.encoding('utf-8))`

### 示例2：yaml文件 -> 字典

```python
import yaml
with open('demo.yaml', encoding='utf-8') as f:   # demo.yaml内容同上例yaml字符串 
    print(yaml.safe_load(f))
```

打印结果同上例。

### 字典 -> yaml字符串或文件

```python
import yaml
dict_var = {'name': 'Cactus', 'age': 18, 'skills': [['Python', 3], ['Java', 5]], 'has_blog': True, 'gf': None}
print(yaml.dump(dict_var,))  # 转为字符串，使用默认flow流格式
with open('demo5.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(dict_var, f, default_flow_style=False)  # 写入文件，不是用flow流格式
```

打印内容：

```python
age: 18
gf: null
has_blog: true
name: Cactus
skills:
- [Python, 3]
- [Java, 5]
```

demo5.yaml文件内容：

```yaml
age: 18
gf: null
has_blog: true
name: Cactus
skills:
- - Python
  - 3
- - Java
  - 5
```

