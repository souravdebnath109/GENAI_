# from langchain_community.tools import DuckDuckGoSearchRun

# search_tool = DuckDuckGoSearchRun()
# result = search_tool.invoke("top 4 destinations  and their universities of bangladeshi students for phd in cse ")
# print("\n")
# print(result)
# print("\n")
# print(search_tool.name)
# print("\n")
# print(search_tool.description)
# print("\n")
# print(search_tool.args)



from langchain_community.tools import ShellTool

shelltool = ShellTool()
result = shelltool.invoke("dir")  # Use 'dir' for Windows
print(result)