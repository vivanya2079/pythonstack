# import zipfile

# with zipfile.ZipFile("mynew.zip", 'w') as zipf:
#     zipf.write("C:/Users/vivan/Music/python programs/vichuu.txt")
#     zipf.write("C:/Users/vivan/Music/python programs/swapu.txt")
#     print("files compressed succesfully")



# import zipfile

# # Open the ZIP file for reading
# with zipfile.ZipFile('mynew.zip', 'r') as zip_file:
#     # List the contents of the ZIP file
#     file_list = zip_file.namelist()
#     print("Contents of the ZIP file:", file_list)



# import zipfile

# # Open the ZIP file for reading
# with zipfile.ZipFile("C:/Users/vivan/Downloads/zipf" , 'r') as zip_file:
#     # List the contents of the ZIP file
#     file_list = zip_file.namelist()
#     print("Contents of the ZIP file:", file_list)

#     # Extract all files from the ZIP archive
#     for file_name in file_list:
#         zip_file.extract(file_name, "C:/Users/vivan/Downloads")
