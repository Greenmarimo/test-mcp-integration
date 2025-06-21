#!/usr/bin/env python3
"""
Демонстрационный скрипт
Создан через MCP интеграцию в Claude Desktop
"""

def main():
    print("🎉 MCP GitHub интеграция работает!")
    print("📝 Этот файл был создан автоматически")
    print("🚀 Теперь вы можете управлять GitHub прямо из Claude")
    
    features = [
        "Создание репозиториев",
        "Создание и редактирование файлов",
        "Управление issues и pull requests",
        "Работа с ветками"
    ]
    
    print("\n✅ Доступные функции:")
    for feature in features:
        print(f"  - {feature}")

if __name__ == "__main__":
    main()
