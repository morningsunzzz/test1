"""Streamlit 应用测试模块"""

import pytest
from src.backend.app import health_check


class TestApp:
    """应用测试类"""

    def test_health_check(self):
        """测试健康检查端点"""
        result = health_check()
        assert isinstance(result, dict)
        assert result["status"] == "healthy"
        assert "message" in result
        assert result["message"] == "BankSys is running"
