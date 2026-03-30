"""数据分析工具模块"""

import pandas as pd
import numpy as np
from typing import Any


class DataAnalyzer:
    """数据分析器"""

    @staticmethod
    def get_summary(df: pd.DataFrame) -> pd.DataFrame:
        """获取数据摘要统计
        
        Args:
            df: 输入 DataFrame
            
        Returns:
            pd.DataFrame: 摘要统计信息
        """
        return df.describe()

    @staticmethod
    def get_missing_info(df: pd.DataFrame) -> pd.DataFrame:
        """获取缺失值信息
        
        Args:
            df: 输入 DataFrame
            
        Returns:
            pd.DataFrame: 缺失值统计
        """
        missing_count = df.isnull().sum()
        missing_percent = (df.isnull().sum() / len(df) * 100).round(2)
        missing_info = pd.DataFrame({
            '缺失数量': missing_count,
            '缺失比例 (%)': missing_percent
        })
        return missing_info[missing_info['缺失数量'] > 0]

    @staticmethod
    def get_column_types(df: pd.DataFrame) -> pd.Series:
        """获取列数据类型
        
        Args:
            df: 输入 DataFrame
            
        Returns:
            pd.Series: 列类型信息
        """
        return df.dtypes

    @staticmethod
    def correlation_matrix(df: pd.DataFrame, method: str = 'pearson') -> pd.DataFrame:
        """计算相关系数矩阵
        
        Args:
            df: 输入 DataFrame
            method: 相关系数计算方法，默认 pearson
            
        Returns:
            pd.DataFrame: 相关系数矩阵
        """
        numeric_df = df.select_dtypes(include=[np.number])
        return numeric_df.corr(method=method)
