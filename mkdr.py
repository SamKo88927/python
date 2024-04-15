import os

directory = "automation/purchase_flow"

test_files = [
    "test_checkout_process.py",
    "test_payment_processing.py",
    "test_order_confirmation.py"
]

# 確認目錄存在或創建目錄
os.makedirs(directory, exist_ok=True)

# 在指定目錄中生成測試案例文件
for file_name in test_files:
    file_path = os.path.join(directory, file_name)
    # 如果文件不存在，則創建文件
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("# Your test code goes here\n")
            file.write("# This is a placeholder for your test case\n")
    print(f"Created file: {file_path}")