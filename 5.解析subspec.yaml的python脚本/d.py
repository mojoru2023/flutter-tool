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

# 遍历当前目录下的所有文件夹
for dir_name in os.listdir('.'):
    if os.path.isdir(dir_name):
        pubspec_path = os.path.join(dir_name, 'pubspec.yaml')

        # 检查是否存在 pubspec.yaml 文件
        if os.path.isfile(pubspec_path):
            with open(pubspec_path, 'r', encoding='utf-8') as file:
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
                        output.write("--"*36)  # 添加空行分隔不同项目
                        output.write("\n")  # 添加空行分隔不同项目

                except yaml.YAMLError as exc:
                    print(f"Error reading {pubspec_path}: {exc}")

print(f"Dependency information has been written to \n {output_file}.")
