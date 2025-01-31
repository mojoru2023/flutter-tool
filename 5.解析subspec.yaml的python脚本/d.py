import os
import yaml
import shutil

# 设置输出文件夹和输出文件名
output_dir = 'flutter_dev_info'
output_file = os.path.join(output_dir, 'info.txt')

# 删除并重新创建输出文件夹
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

def process_pubspec(file_path):
    """处理 pubspec.yaml 文件，提取项目信息"""
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            # 读取 YAML 文件内容
            pubspec_content = yaml.safe_load(file)

            project_name = pubspec_content.get('name', 'Unnamed Project')
            dependencies = pubspec_content.get('dependencies', {})
            dev_dependencies = pubspec_content.get('dev_dependencies', {})

            # 写入项目信息到输出文件
            with open(output_file, 'a', encoding='utf-8') as output:
                output.write(f"Project: {project_name}\n")
                output.write("Dependencies:\n")
                for dep, version in dependencies.items():
                    output.write(f"  - {dep}: {version}\n")
                output.write("Dev Dependencies:\n")
                for dev_dep, version in dev_dependencies.items():
                    output.write(f"  - {dev_dep}: {version}\n")
                output.write("--" * 36)  # 添加分隔线
                output.write("\n")  # 添加空行分隔不同项目

        except yaml.YAMLError as exc:
            print(f"Error reading {file_path}: {exc}")

def find_pubspecs(start_dir):
    """递归遍历目录，寻找 pubspec.yaml 文件"""
    for dirpath, _, files in os.walk(start_dir):
        if 'pubspec.yaml' in files:
            pubspec_path = os.path.join(dirpath, 'pubspec.yaml')
            process_pubspec(pubspec_path)

# 从当前工作目录开始搜索
find_pubspecs('.')

print(f"Dependency information has been written to \n{output_file}.")
