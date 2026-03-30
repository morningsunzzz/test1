# 🏦 银行数据分析系统 (BankSys)

基于 Streamlit 构建的交互式银行数据分析系统。

## 📋 项目简介

BankSys 是一个功能完整的银行数据分析系统，提供数据加载、统计分析、可视化展示等功能，帮助银行从业人员快速理解和分析业务数据。

## ✨ 主要功能

- 📊 **数据概览**：快速查看数据基本统计信息
- 📈 **统计分析**：缺失值分析、描述性统计、相关性分析
- 📉 **可视化分析**：
  - 特征相关性热力图
  - 分布直方图
  - 散点图分析
- 💾 **数据导出**：支持导出分析结果为 CSV 格式
- 🔍 **健康检查**：提供 `/health` 端点用于服务监控

## 🚀 快速开始

### 环境要求

- Python 3.11+
- Conda（推荐）

### 本地安装

```bash
# 创建 conda 虚拟环境
conda create -n banksysenv python=3.11 -y
conda activate banksysenv

# 安装项目依赖
pip install -e .

# 或使用开发模式（包含测试和代码质量工具）
pip install -e ".[dev]"
```

### 启动应用

```bash
# 方式 1：使用 streamlit 命令
streamlit run src/backend/app.py --server.port=8502 --server.address=0.0.0.0

# 方式 2：直接运行 Python 脚本
python src/backend/app.py
```

应用将在 **http://localhost:8502** 启动。

### Docker 部署

```bash
# 构建镜像
docker build -t banksys .

# 运行容器
docker run -p 8502:8502 banksys
```

## 📁 项目结构

```
banksys/
├── .github/workflows/ci.yml    # CI 工作流配置
├── src/
│   ├── backend/
│   │   ├── __init__.py
│   │   └── app.py              # Streamlit 主应用
│   ├── core/
│   │   ├── __init__.py
│   │   └── data_loader.py      # 数据加载模块
│   └── utils/
│       ├── __init__.py
│       └── analyzer.py         # 数据分析工具
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py     # 数据加载器测试
│   ├── test_analyzer.py        # 分析器测试
│   └── test_app.py             # 应用测试
├── .dockerignore
├── .gitattributes
├── .gitignore
├── Dockerfile
├── pyproject.toml              # 项目配置
└── README.md
```

## 🧪 测试

```bash
# 运行测试并生成覆盖率报告
pytest

# 运行测试并查看覆盖率详情
pytest --cov=src --cov-report=html

# 运行特定测试文件
pytest tests/test_data_loader.py -v
```

### 代码质量检查

```bash
# 代码格式化检查
black --check src/ tests/

# 代码风格检查
ruff check src/ tests/

# 类型检查
mypy src/ --ignore-missing-imports
```

## 📊 数据格式

支持以下数据格式：
- CSV 文件（`.csv`）
- Excel 文件（`.xlsx`, `.xls`）

将数据文件放入项目根目录的 `data/` 文件夹中，应用会自动识别。

## 🔧 配置说明

### 端口配置

默认监听端口：**8502**

修改端口：
```bash
streamlit run src/backend/app.py --server.port=YOUR_PORT
```

### 数据目录配置

在应用侧边栏中可以配置数据目录路径，默认为项目根目录下的 `data/` 文件夹。

## 🛠️ 开发工具

项目已集成以下开发工具：

- **pytest**: 测试框架
- **black**: 代码格式化
- **ruff**: 代码风格检查
- **mypy**: 类型检查
- **pytest-cov**: 测试覆盖率

## 📝 开发规范

### 代码风格

- 遵循 PEP 8 规范
- 使用 black 格式化代码（line-length=88）
- 使用 ruff 进行代码风格检查
- 所有代码使用 LF 换行符

### 提交规范

```
feat: 新功能
fix: 修复 bug
docs: 文档更新
style: 代码格式调整
refactor: 重构代码
test: 测试相关
chore: 构建/工具链相关
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📧 联系方式

- GitHub: [@morningsunzzz](https://github.com/morningsunzzz)
- 仓库：[https://github.com/morningsunzzz/test1](https://github.com/morningsunzzz/test1)

---

**版本**: v0.1.0  
**构建时间**: 2026-03-30
