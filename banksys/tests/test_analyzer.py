"""数据分析器测试模块"""

import pytest
import pandas as pd
import numpy as np
from src.utils.analyzer import DataAnalyzer


class TestDataAnalyzer:
    """数据分析器测试类"""

    @pytest.fixture
    def sample_df(self):
        """创建示例 DataFrame"""
        return pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [2.0, 4.0, 6.0, 8.0, 10.0],
            'C': ['x', 'y', 'z', 'w', 'v']
        })

    @pytest.fixture
    def df_with_missing(self):
        """创建带缺失值的 DataFrame"""
        return pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [None, 4.0, 6.0, None, 10.0],
            'C': ['x', 'y', 'z', 'w', 'v']
        })

    def test_get_summary(self, sample_df):
        """测试获取摘要统计"""
        summary = DataAnalyzer.get_summary(sample_df)
        assert isinstance(summary, pd.DataFrame)
        assert 'A' in summary.columns
        assert 'B' in summary.columns
        assert summary.loc['count', 'A'] == 5.0

    def test_get_missing_info_no_missing(self, sample_df):
        """测试无缺失值的情况"""
        missing_info = DataAnalyzer.get_missing_info(sample_df)
        assert len(missing_info) == 0

    def test_get_missing_info_with_missing(self, df_with_missing):
        """测试有缺失值的情况"""
        missing_info = DataAnalyzer.get_missing_info(df_with_missing)
        assert len(missing_info) > 0
        assert 'A' in missing_info.index or 'B' in missing_info.index
        assert '缺失数量' in missing_info.columns
        assert '缺失比例 (%)' in missing_info.columns

    def test_get_column_types(self, sample_df):
        """测试获取列类型"""
        col_types = DataAnalyzer.get_column_types(sample_df)
        assert isinstance(col_types, pd.Series)
        assert len(col_types) == 3
        assert col_types['A'] in ['int64', 'int32']
        assert col_types['B'] in ['float64', 'float32']

    def test_correlation_matrix(self, sample_df):
        """测试相关系数矩阵"""
        corr_matrix = DataAnalyzer.correlation_matrix(sample_df)
        assert isinstance(corr_matrix, pd.DataFrame)
        assert 'A' in corr_matrix.columns
        assert 'B' in corr_matrix.columns
        assert corr_matrix.loc['A', 'A'] == 1.0
        assert corr_matrix.loc['B', 'B'] == 1.0

    def test_correlation_matrix_spearman(self, sample_df):
        """测试 Spearman 相关系数"""
        corr_matrix = DataAnalyzer.correlation_matrix(sample_df, method='spearman')
        assert isinstance(corr_matrix, pd.DataFrame)
        assert corr_matrix.loc['A', 'A'] == 1.0

    def test_correlation_matrix_only_numeric(self, sample_df):
        """测试相关系数矩阵只包含数值列"""
        corr_matrix = DataAnalyzer.correlation_matrix(sample_df)
        assert 'C' not in corr_matrix.columns
