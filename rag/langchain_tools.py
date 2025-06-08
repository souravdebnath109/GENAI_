


from langchain_community.tools import ShellTool

shelltool = ShellTool()
result = shelltool.invoke("dir")  # Use 'dir' for Windows
print(result)