"""数据加载器测试模块"""

import pytest
import pandas as pd
from pathlib import Path
from src.core.data_loader import DataLoader


class TestDataLoader:
    """数据加载器测试类"""

    def test_init_default(self):
        """测试默认初始化"""
        loader = DataLoader()
        assert loader.data_dir is not None
        assert isinstance(loader.data_dir, Path)

    def test_init_custom_path(self):
        """测试自定义路径初始化"""
        custom_path = "/custom/data"
        loader = DataLoader(custom_path)
        assert str(loader.data_dir) == custom_path

    def test_get_available_files_empty(self):
        """测试空数据目录"""
        loader = DataLoader("/nonexistent/path")
        files = loader.get_available_files()
        assert isinstance(files, list)
        assert len(files) == 0

    def test_load_csv_file_not_found(self):
        """测试 CSV 文件不存在"""
        loader = DataLoader("/nonexistent/path")
        with pytest.raises(FileNotFoundError):
            loader.load_csv("nonexistent.csv")

    def test_load_excel_file_not_found(self):
        """测试 Excel 文件不存在"""
        loader = DataLoader("/nonexistent/path")
        with pytest.raises(FileNotFoundError):
            loader.load_excel("nonexistent.xlsx")
