import os
import sys
import subprocess
import re
import tempfile

def extract_code(text):
    """
    Извлекает первый блок Python-кода из текста ответа.
    """
    pattern = r"```(?:python)?(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def run_code(response_text):
    """
    Создает временный файл, записывает в него код, выполняет и выводит результат.
    """
    code = extract_code(response_text)
    
    if not code:
        sys.stdout.write("\033[31m[Sandbox Error]: Не найден блок кода для выполнения.\033[0m\n")
        return
        
    fd, path = tempfile.mkstemp(suffix=".py", text=True)
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(code)
            
        sys.stdout.write("\033[36m[Sandbox Output]:\033[0m\n")
        sys.stdout.write("\033[90m" + "-" * 40 + "\033[0m\n")
        
        result = subprocess.run(
            [sys.executable, path],
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            sys.stdout.write(result.stdout)
            
        if result.stderr:
             sys.stdout.write(f"\033[31m{result.stderr}\033[0m")
             
        if not result.stdout and not result.stderr:
             sys.stdout.write("\033[90m(Скрипт выполнен без вывода в консоль)\033[0m\n")
             
        sys.stdout.write("\033[90m" + "-" * 40 + "\033[0m\n")
        
    except Exception as e:
        sys.stdout.write(f"\033[31m[Sandbox Exception]: {str(e)}\033[0m\n")
    finally:
        if os.path.exists(path):
            os.remove(path)
