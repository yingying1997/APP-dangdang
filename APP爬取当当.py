import requests # 导入 requests 模块，用于发送网络请求
# pip install rich
from rich import print as rprint # 导入 rich 模块的 print 函数，用于打印带样式的输出

# 目标 url
url = 'http://mapi7.dangdang.com/index.php?page_version=new2&access-token=&time_code=0a700316b85a0d578709bd673dd123dc&img_size=e&client_version=10.12.4&pageSize=10&union_id=537-100998&timestamp=1687961723&province_id=111&permanent_id=20230628220338845805790296886915991&a=all-search&global_province_id=111&page_action=search&c=search&sort_type=default_0&keyword=%E7%88%AC%E8%99%AB&udid=4aa439184898c3fbab8ed2cd869b77e1&user_client=android&page=1'

# 发送 get 请求，获取响应对象
res = requests.get(url)

# 使用 rich 模块的 print 函数打印响应对象中的 JSON 数据的 product 字段
# rprint(res.json()['data']['product']) # 返回的数据类型 list

# 获取响应对象中的 product 列表
product_lst = res.json()['data']['product']

# 遍历 product 列表
for product in product_lst:
    # 创建字典
    item = {}
    item['title'] = product.get('productName') # 获取商品名称
    item['author'] = product.get('author') # 获取商品作者
    item['publisher'] = product.get('publisher') # 获取商品出版社
    item['commentCount'] = product.get('commentCount') # 获取商品评论数
    item['price'] = product.get('price') # 获取商品价格
    print(item) # 打印商品信息
    print('-' * 100) # 分隔线