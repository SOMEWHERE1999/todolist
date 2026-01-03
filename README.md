# todolist

一个采用 Flask + SQLAlchemy 的前后端分离示例，演示了 MSV 架构与连接本地 MySQL 数据库的待办事项应用。

## 项目结构
```
web-project-(flask+sqlalchemy)-start1/
├── app/
│   ├── __init__.py            # 应用工厂函数、路由定义
│   ├── static/                # 静态资源
│   │   ├── css/
│   │   └── js/
│   └── templates/
│       └── index.html         # 前端页面（AngularJS）
├── config/
│   ├── __init__.py
│   ├── config.py              # 数据库连接配置
│   └── sct.sql                # 数据库脚本副本
├── controller/
│   ├── __init__.py
│   ├── userController.py      # 用户业务逻辑
│   └── todolistController.py  # 待办事项业务逻辑
├── database/
│   └── sct.sql                # 数据库结构和初始数据
├── models/
│   ├── __init__.py            # SQLAlchemy 实例
│   ├── todolist.py            # 待办事项模型
│   └── user.py                # 用户模型
├── utils/
│   ├── commons.py             # 通用响应
│   ├── error.py               # 错误处理
│   ├── loggings.py            # 日志记录
│   ├── response_code.py       # 响应状态码定义
│   └── rsa_encryption_decryption.py  # RSA 简易工具
├── requirements.txt           # 依赖
└── start.py                   # 应用入口
```

## 快速开始
1. 安装依赖
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. 初始化数据库（确保本地 MySQL 已启动并可连接）
   ```bash
   mysql -u root -p < database/sct.sql
   ```
3. 配置数据库连接（可选）
   - 通过环境变量 `DATABASE_URI` 指定连接串，例如：
     `mysql+pymysql://user:password@localhost:3306/todolist?charset=utf8mb4`
4. 运行应用
   ```bash
   python start.py
   ```
5. 在浏览器访问 `http://localhost:5000`，即可体验前后端分离的待办列表。

## 接口说明（示例）
- `GET /api/todos/`：获取待办列表
- `POST /api/todos/`：创建待办事项，JSON 示例 `{ "title": "Call Mary" }`
- `PUT /api/todos/<id>`：更新待办事项
- `DELETE /api/todos/<id>`：删除待办事项（软删除，设置 `IsDelete` 标记）

用户接口仅用于演示注册/登录：
- `POST /api/users/register`、`POST /api/users/login`
