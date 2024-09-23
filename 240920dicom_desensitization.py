# LIFANGU 20240918
# 这是一个用于给DICOM文件批量脱敏的工具，会将目标目录下所有的.dcm文件脱敏, 并原路径保存. 注意修改测试路径! 慎重使用该软件!
# 更改目录时注意更改这个目录的Patient ID
import pydicom
import os

def modify_dicom_tags(dicom_file, tags_and_values, output_file=None):
    # 读取 DICOM 文件
    ds = pydicom.dcmread(dicom_file)

    # 修改指定 tags 的值
    for tag, new_value in tags_and_values:
        try:
            print(f"Modifying Tag {tag} ({ds[tag].name}) from {ds[tag].value} to {new_value}")
            ds[tag].value = new_value
        except KeyError:
            print(f"Tag {tag} NOT in this DICOM file")

            # 保存修改后的 DICOM 文件
    if output_file is None:
        output_file = dicom_file  # 如果不指定输出文件路径，覆盖原文件

    ds.save_as(output_file)
    print(f"Desensitization: {output_file}")

def desensitize_dicom_folder(folder_path, tags_and_values):

    for filename in os.listdir(folder_path):
        if filename.endswith(".dcm"):
            dicom_file_path = os.path.join(folder_path, filename)
            print(f"Processing file: {dicom_file_path}")
            modify_dicom_tags(dicom_file_path, tags_and_values)

# 设置脱敏的DICOM tags和值
tags_to_modify = [
    ((0x0008, 0x0080), 'NA'),  # Institution Name
    ((0x0008, 0x0081), 'NA'),  # Institution Address
    ((0x0008, 0x0090), 'NA'),  # Referring Physician Name
    ((0x0008, 0x1070), 'NA'),  # Operator's Name
    ((0x0010, 0x1040), 'NA'),  # Patient's Address
    ((0x0010, 0x2154), 'NA'),  # Patient's Telephone Numbers
    ((0x0010, 0x1001), 'NA'),  # Other Patient Names
    ((0x0010, 0x1000), 'NA'),  # Other Patient IDs
    ((0x0010, 0x1002), ''),  # Other Patient IDs Sequence
    ((0x0010, 0x0010), 'NA'),  # Patient's Name
    ((0x0010, 0x0020), 'XJTU-FWH01_005') ] # Patient ID

# 设定DICOM文件所在的文件夹
folder_path = r"C:\Users\lifan\Desktop\test240922\case05"

# 调用函数进行脱敏处理
desensitize_dicom_folder(folder_path, tags_to_modify)