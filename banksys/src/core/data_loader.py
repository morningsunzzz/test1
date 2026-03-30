"""银行数据加载与处理模块"""

from pathlib import Path
import pandas as pd
from typing import Optional


class DataLoader:
    """数据加载器"""

    def __init__(self, data_dir: Optional[str] = None):
        """初始化数据加载器
        
        Args:
            data_dir: 数据目录路径，默认为当前目录下的 data 文件夹
        """
        if data_dir:
            self.data_dir = Path(data_dir)
        else:
            self.data_dir = Path(__file__).parent.parent.parent.parent / "data"

    def load_csv(self, filename: str) -> pd.DataFrame:
        """加载 CSV 文件
        
        Args:
            filename: CSV 文件名
            
        Returns:
            DataFrame: 加载的数据
        """
        file_path = self.data_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在：{file_path}")
        return pd.read_csv(file_path)

    def load_excel(self, filename: str, sheet_name: Optional[str] = None) -> pd.DataFrame:
        """加载 Excel 文件
        
        Args:
            filename: Excel 文件名
            sheet_name: 工作表名称，默认为第一个工作表
            
        Returns:
            DataFrame: 加载的数据
        """
        file_path = self.data_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在：{file_path}")
        return pd.read_excel(file_path, sheet_name=sheet_name)

    def get_available_files(self) -> list[str]:
        """获取数据目录中可用的文件列表
        
        Returns:
            list[str]: 文件名列表
        """
        if not self.data_dir.exists():
            return []
        return [f.name for f in self.data_dir.iterdir() if f.is_file()]
