from handlers.imageHandler import ImageHandler

if __name__ == '__main__':
    # client = DoubaoClient()
    # messages = [
    #     {"role": "user", "content": "你好"}
    # ]
    #
    # # 测试大模型调用
    # resp = client.call(messages)
    # print(resp)

     #    input_s = """git init 初始化仓库 git clone [url] 克隆远程库 git add [file] 添加文件到暂存区 git commit -m "msg" 提交到本地仓库 git status 查看状态 git pull 拉取远程更新 git push 推送本地提交 git branch 查看分支 git checkout -b [branch] 创建切换分支 git merge [branch] 合并分支 git log 查看提交历史 git reset --hard [commit] 版本回退 git stash 临时保存修改
     # .gitignore 定义忽略文件"""
     #
     #    handler = TXTHandler('multimodal_store.csv')
     #    handler.handle(input_s)

    # handler = UrlHandler('multimodal_store.csv')
    #
    # # 测试大模型调用
    # resp = handler.handle("https://zhuanlan.zhihu.com/p/637960746")

    handler = ImageHandler('multimodal_store.csv')
    resp = handler.handle("/Users/rain/Project/llm/favorbot/data/images/test1.png", "收藏")
    print(resp)







