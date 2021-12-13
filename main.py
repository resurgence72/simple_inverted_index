import time
from mock import Mock, Express
from inverted_index import InvertIndex

if __name__ == '__main__':
    start = time.time()

    # mock ecs 数据
    invert_index_mock = Mock(max_num=20000)
    ecs_objs = invert_index_mock.mock_ecs_objs()
    print('ecs mock 对象耗时: ', time.time() - start)

    ii = InvertIndex()

    # 构建倒排索引
    start = time.time()
    for obj in ecs_objs:
        # 将需要构建的 kv 组合成 dict 类型
        tags = obj.tags
        # 将添加 ip 信息到 labels
        tags.update({'ip': obj.ip})
        # 需要指定当前 labels 所对应的唯一 pk
        ii.create_invert_index(obj.pk, obj.tags)
    print('构建倒排索引耗时: ', time.time() - start)

    # 打印当前倒排索引
    ii.show_invert_index()

    # mock 请求体
    exp = Express()

    """
    此次请求含义：
    获取: 1. regain 为 beijing 的
         2. 且 type 不为 dev 的
         3. 且 ip 不已 4/5/6 结尾的 ecs pks
    
    如果加上 target_label 参数表示将结果根据 group 做分组统计
    """
    req = {
        'labels': [
            {'type': exp.eq, 'key': 'regain', 'value': 'beijing'},
            {'type': exp.ne, 'key': 'type', 'value': 'dev'},
            {'type': exp.rex, 'key': 'ip', 'value': '.*[456]$'},
        ],
        # 'target_label': 'group'  # 做group_by才时需要打开，比如将match结果按照 group 维度做分组统计
    }

    start = time.time()
    # target_label 不存在，即为从倒排索引中拿匹配pks;
    # target_label 存在，则根据 target_label 做 group_by
    match_result = ii.find_match_pks_by_labels(
        req.get('labels'),
        req.get('target_label')
    )
    print('find_match_pks_by_labels', time.time() - start)
    print("match_result: ", match_result)
